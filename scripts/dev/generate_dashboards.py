import json
import os

DASHBOARDS_DIR = os.path.join(os.path.dirname(__file__), 'dashboards')

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def generate_system_health_dashboard():
    dashboard = {
        "id": None,
        "uid": "system-health",
        "title": "System Health",
        "tags": ["system", "health"],
        "timezone": "browser",
        "schemaVersion": 30,
        "version": 0,
        "panels": [
            {
                "id": 1,
                "title": "CPU Usage",
                "type": "timeseries",
                "gridPos": {"h": 8, "w": 12, "x": 0, "y": 0},
                "targets": [
                    {
                        "expr": "100 - (avg by (instance) (rate(node_cpu_seconds_total{mode='idle'}[5m])) * 100)",
                        "legendFormat": "{{instance}}",
                        "refId": "A"
                    }
                ],
                "fieldConfig": {
                    "defaults": {
                        "unit": "percent",
                        "min": 0,
                        "max": 100
                    }
                }
            },
            {
                "id": 2,
                "title": "Memory Usage",
                "type": "timeseries",
                "gridPos": {"h": 8, "w": 12, "x": 12, "y": 0},
                "targets": [
                    {
                        "expr": "(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100",
                        "legendFormat": "{{instance}}",
                        "refId": "A"
                    }
                ],
                "fieldConfig": {
                    "defaults": {
                        "unit": "percent",
                        "min": 0,
                        "max": 100
                    }
                }
            },
            {
                "id": 3,
                "title": "Service Uptime",
                "type": "stat",
                "gridPos": {"h": 4, "w": 24, "x": 0, "y": 8},
                "targets": [
                    {
                        "expr": "up",
                        "legendFormat": "{{instance}}",
                        "refId": "A"
                    }
                ]
            }
        ]
    }
    return dashboard

def generate_business_metrics_dashboard():
    dashboard = {
        "id": None,
        "uid": "business-metrics",
        "title": "Business Metrics",
        "tags": ["business", "kpi"],
        "timezone": "browser",
        "schemaVersion": 30,
        "version": 0,
        "panels": [
            {
                "id": 1,
                "title": "Total Revenue",
                "type": "stat",
                "gridPos": {"h": 6, "w": 8, "x": 0, "y": 0},
                "targets": [
                    {
                        "expr": "sum(business_metric_revenue_total)",
                        "legendFormat": "Revenue",
                        "refId": "A"
                    }
                ],
                "fieldConfig": {
                    "defaults": {
                        "unit": "currencyUSD"
                    }
                }
            },
            {
                "id": 2,
                "title": "Active Users",
                "type": "stat",
                "gridPos": {"h": 6, "w": 8, "x": 8, "y": 0},
                "targets": [
                    {
                        "expr": "business_metric_active_users",
                        "legendFormat": "Users",
                        "refId": "A"
                    }
                ]
            },
            {
                "id": 3,
                "title": "Order Volume",
                "type": "timeseries",
                "gridPos": {"h": 8, "w": 24, "x": 0, "y": 6},
                "targets": [
                    {
                        "expr": "rate(business_metric_orders_total[5m])",
                        "legendFormat": "Orders/sec",
                        "refId": "A"
                    }
                ]
            }
        ]
    }
    return dashboard

if __name__ == "__main__":
    ensure_dir(DASHBOARDS_DIR)
    
    system_dashboard = generate_system_health_dashboard()
    with open(os.path.join(DASHBOARDS_DIR, 'system_health.json'), 'w') as f:
        json.dump(system_dashboard, f, indent=2)
    print(f"Generated system_health.json in {DASHBOARDS_DIR}")

    business_dashboard = generate_business_metrics_dashboard()
    with open(os.path.join(DASHBOARDS_DIR, 'business_metrics.json'), 'w') as f:
        json.dump(business_dashboard, f, indent=2)
    print(f"Generated business_metrics.json in {DASHBOARDS_DIR}")
