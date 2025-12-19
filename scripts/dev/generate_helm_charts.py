import yaml
import os
import shutil
from pathlib import Path

# Configuration
DOCKER_COMPOSE_FILE = "docker-compose.yml"
CHARTS_DIR = "charts"
REGISTRY_PREFIX = "analytics-engine" # Example registry
CHART_VERSION = "0.1.0"

def load_compose_config(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def clean_charts_dir(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)

def generate_chart_yaml(service_name):
    return f"""apiVersion: v2
name: {service_name}
description: A Helm chart for Kubernetes
type: application
version: {CHART_VERSION}
appVersion: "{CHART_VERSION}"
"""

def generate_values_yaml(service_name, service_config):
    # Extract env vars
    env_vars = service_config.get("environment", [])
    env_dict = {}
    if isinstance(env_vars, list):
        for item in env_vars:
            if "=" in item:
                k, v = item.split("=", 1)
                env_dict[k] = v
            else:
                env_dict[item] = "" # Empty if from host
    elif isinstance(env_vars, dict):
        env_dict = env_vars

    # Extract ports
    ports = service_config.get("ports", [])
    service_port = 80
    target_port = 8000
    
    if ports:
        # Take the first mapped port
        p = ports[0]
        if isinstance(p, str):
            if ":" in p:
                parts = p.split(":")
                service_port = int(parts[0])
                target_port = int(parts[1])
            else:
                service_port = int(p)
                target_port = int(p)
    
    # Image handling
    image_repository = f"{REGISTRY_PREFIX}/{service_name}"
    image_tag = "latest"
    if "image" in service_config:
        img_parts = service_config["image"].split(":")
        image_repository = img_parts[0]
        if len(img_parts) > 1:
            image_tag = img_parts[1]

    values = {
        "replicaCount": 1,
        "image": {
            "repository": image_repository,
            "pullPolicy": "IfNotPresent",
            "tag": image_tag
        },
        "service": {
            "type": "ClusterIP",
            "port": service_port,
            "targetPort": target_port
        },
        "env": env_dict,
        "resources": {
            "limits": {
                "cpu": "500m",
                "memory": "512Mi"
            },
            "requests": {
                "cpu": "100m",
                "memory": "128Mi"
            }
        },
        "autoscaling": {
            "enabled": False,
            "minReplicas": 1,
            "maxReplicas": 10,
            "targetCPUUtilizationPercentage": 80
        }
    }
    return yaml.dump(values, default_flow_style=False)

def generate_dev_values_yaml(service_name):
    """Generate values-dev.yaml with development settings."""
    values = {
        "replicaCount": 1,
        "image": {
            "pullPolicy": "IfNotPresent",
            "tag": "latest"
        },
        "resources": {
            "limits": {
                "cpu": "250m",
                "memory": "256Mi"
            },
            "requests": {
                "cpu": "50m",
                "memory": "64Mi"
            }
        },
        "env": {
            "DEBUG": "true",
            "LOG_LEVEL": "DEBUG"
        }
    }
    return yaml.dump(values, default_flow_style=False)

def generate_prod_values_yaml(service_name):
    """Generate values-prod.yaml with production settings."""
    values = {
        "replicaCount": 2,
        "image": {
            "pullPolicy": "Always",
            # tag should be specific version in prod
        },
        "autoscaling": {
            "enabled": True,
            "minReplicas": 2,
            "maxReplicas": 10,
            "targetCPUUtilizationPercentage": 75
        },
        "resources": {
            "limits": {
                "cpu": "1000m",
                "memory": "1Gi"
            },
            "requests": {
                "cpu": "500m",
                "memory": "512Mi"
            }
        },
        "env": {
            "DEBUG": "false",
            "LOG_LEVEL": "INFO"
        }
    }
    return yaml.dump(values, default_flow_style=False)

def generate_deployment_yaml(service_name):
    return """apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "chart.fullname" . }}
  labels:
    {{- include "chart.labels" . | nindent 4 }}
spec:
  {{- if not .Values.autoscaling.enabled }}
  replicas: {{ .Values.replicaCount }}
  {{- end }}
  selector:
    matchLabels:
      {{- include "chart.selectorLabels" . | nindent 6 }}
  template:
    metadata:
      {{- with .Values.podAnnotations }}
      annotations:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      labels:
        {{- include "chart.selectorLabels" . | nindent 8 }}
    spec:
      {{- with .Values.imagePullSecrets }}
      imagePullSecrets:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      securityContext:
        {{- toYaml .Values.podSecurityContext | nindent 8 }}
      containers:
        - name: {{ .Chart.Name }}
          securityContext:
            {{- toYaml .Values.securityContext | nindent 12 }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag | default .Chart.AppVersion }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          ports:
            - name: http
              containerPort: {{ .Values.service.targetPort }}
              protocol: TCP
          envFrom:
            - configMapRef:
                name: {{ include "chart.fullname" . }}-env
          resources:
            {{- toYaml .Values.resources | nindent 12 }}
"""

def generate_service_yaml(service_name):
    return """apiVersion: v1
kind: Service
metadata:
  name: {{ include "chart.fullname" . }}
  labels:
    {{- include "chart.labels" . | nindent 4 }}
spec:
  type: {{ .Values.service.type }}
  ports:
    - port: {{ .Values.service.port }}
      targetPort: {{ .Values.service.targetPort }}
      protocol: TCP
      name: http
  selector:
    {{- include "chart.selectorLabels" . | nindent 4 }}
"""

def generate_configmap_yaml(service_name):
    return """apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ include "chart.fullname" . }}-env
  labels:
    {{- include "chart.labels" . | nindent 4 }}
data:
  {{- range $key, $val := .Values.env }}
  {{ $key }}: {{ $val | quote }}
  {{- end }}
"""

def generate_helpers_tpl(service_name):
    return """{{/*
Expand the name of the chart.
*/}}
{{- define "chart.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "chart.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "chart.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "chart.labels" -}}
helm.sh/chart: {{ include "chart.chart" . }}
{{ include "chart.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "chart.selectorLabels" -}}
app.kubernetes.io/name: {{ include "chart.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
"""

def main():
    print(f"Reading {DOCKER_COMPOSE_FILE}...")
    compose_config = load_compose_config(DOCKER_COMPOSE_FILE)
    
    clean_charts_dir(CHARTS_DIR)
    
    services = compose_config.get("services", {})
    print(f"Found {len(services)} services. Generating charts...")
    
    for service_name, config in services.items():
        print(f"Generating chart for {service_name}...")
        
        service_chart_dir = os.path.join(CHARTS_DIR, service_name)
        templates_dir = os.path.join(service_chart_dir, "templates")
        
        os.makedirs(templates_dir)
        
        # Write Chart.yaml
        with open(os.path.join(service_chart_dir, "Chart.yaml"), "w") as f:
            f.write(generate_chart_yaml(service_name))
            
        # Write values.yaml
        with open(os.path.join(service_chart_dir, "values.yaml"), "w") as f:
            f.write(generate_values_yaml(service_name, config))
            
        # Write values-dev.yaml
        with open(os.path.join(service_chart_dir, "values-dev.yaml"), "w") as f:
            f.write(generate_dev_values_yaml(service_name))
            
        # Write values-prod.yaml
        with open(os.path.join(service_chart_dir, "values-prod.yaml"), "w") as f:
            f.write(generate_prod_values_yaml(service_name))
            
        # Write templates
        with open(os.path.join(templates_dir, "deployment.yaml"), "w") as f:
            f.write(generate_deployment_yaml(service_name))
            
        with open(os.path.join(templates_dir, "service.yaml"), "w") as f:
            f.write(generate_service_yaml(service_name))
            
        with open(os.path.join(templates_dir, "configmap.yaml"), "w") as f:
            f.write(generate_configmap_yaml(service_name))
            
        with open(os.path.join(templates_dir, "_helpers.tpl"), "w") as f:
            f.write(generate_helpers_tpl(service_name))
            
    print("Chart generation completed!")

if __name__ == "__main__":
    main()
