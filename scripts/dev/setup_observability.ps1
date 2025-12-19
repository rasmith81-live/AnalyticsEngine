<#
.SYNOPSIS
    Sets up the Observability Stack (Prometheus, Grafana, Jaeger) using Helm on a local Kubernetes cluster.
    Also provides options to generate default dashboards.

.DESCRIPTION
    This script automates the deployment of the observability stack.
    Prerequisites: helm, kubectl, and a running Kubernetes cluster (e.g., Docker Desktop, Minikube).

.PARAMETER Install
    Switch to install/upgrade the stack.

.PARAMETER Namespace
    Kubernetes namespace to install into. Default: 'monitoring'.

.PARAMETER GenerateDashboards
    Switch to generate default Grafana dashboards.

.EXAMPLE
    .\setup_observability.ps1 -Install
    .\setup_observability.ps1 -GenerateDashboards
#>

param (
    [switch]$Install,
    [string]$Namespace = "monitoring",
    [switch]$GenerateDashboards
)

$ErrorActionPreference = "Stop"

function Write-Log {
    param ([string]$Message)
    Write-Host "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $Message" -ForegroundColor Cyan
}

function Check-Command {
    param ([string]$Name)
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        Write-Error "$Name is required but not found in PATH."
    }
}

if ($GenerateDashboards) {
    Write-Log "Generating Grafana Dashboards..."
    python "$PSScriptRoot/generate_dashboards.py"
    if ($LASTEXITCODE -eq 0) {
        Write-Log "Dashboards generated successfully."
    } else {
        Write-Error "Failed to generate dashboards."
    }
}

if ($Install) {
    Check-Command "helm"
    Check-Command "kubectl"

    Write-Log "Checking Kubernetes connection..."
    kubectl cluster-info
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Cannot connect to Kubernetes cluster."
    }

    # Create Namespace
    Write-Log "Ensuring namespace '$Namespace' exists..."
    kubectl create namespace $Namespace --dry-run=client -o yaml | kubectl apply -f -

    # Add Helm Repos
    Write-Log "Adding Helm repositories..."
    helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
    helm repo add grafana https://grafana.github.io/helm-charts
    helm repo add jaegertracing https://jaegertracing.github.io/helm-charts
    helm repo update

    # Install Prometheus Stack (includes Operator, Grafana, Alertmanager)
    Write-Log "Installing/Upgrading kube-prometheus-stack..."
    helm upgrade --install prometheus prometheus-community/kube-prometheus-stack `
        --namespace $Namespace `
        --set grafana.enabled=true `
        --set prometheus.prometheusSpec.serviceMonitorSelectorNilUsesHelmValues=false

    # Install Jaeger
    Write-Log "Installing/Upgrading Jaeger..."
    helm upgrade --install jaeger jaegertracing/jaeger `
        --namespace $Namespace `
        --set provisionDataStore.cassandra=false `
        --set allInOne.enabled=true

    Write-Log "Observability Stack setup complete."
    Write-Log "Grafana: kubectl port-forward svc/prometheus-grafana 3000:80 -n $Namespace"
    Write-Log "Prometheus: kubectl port-forward svc/prometheus-kube-prometheus-prometheus 9090:9090 -n $Namespace"
    Write-Log "Jaeger: kubectl port-forward svc/jaeger-query 16686:16686 -n $Namespace"
}

if (-not $Install -and -not $GenerateDashboards) {
    Get-Help $MyInvocation.MyCommand.Path -Detailed
}
