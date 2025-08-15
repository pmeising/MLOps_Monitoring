# Centralized Monitoring Stack

A comprehensive monitoring solution for FastAPI services using Prometheus and Grafana.

## Overview

This monitoring stack provides centralized observability for your FastAPI services:
- **Whisper API (STT)**: Speech-to-Text service monitoring
- **Kokoro API (TTS)**: Text-to-Speech service monitoring
- **Prometheus**: Metrics collection and storage
- **Grafana**: Visualization and dashboards

## Configuration Management

### Dynamic Prometheus Configuration

This monitoring stack includes a dynamic configuration system:

1. **`endpoints.yaml`** - Define your service endpoints:
```yaml
endpoints:
  - ip: localhost
    port: 8000
    name: liquidai
    service_type: fastapi
    description: "LiquidAI LFM2-350M Language Model"
  - ip: localhost
    port: 8001
    name: whisper
    service_type: fastapi
    description: "Whisper Speech-to-Text"
```

2. **`generate_prometheus.py`** - Automatically generates `prometheus.yml`:
```bash
python generate_prometheus.py
```

### Service Types Supported:
- **`fastapi`** - FastAPI services with `/metrics` endpoints
- **`mlflow_server`** - MLFlow tracking server
- **`mlflow_training`** - MLFlow training pipelines

### Adding New Services:

1. Add your service to `endpoints.yaml`
2. Run `python generate_prometheus.py`
3. Restart the monitoring stack

## Quick Start

### Prerequisites
- Docker and Docker Compose installed
- Your FastAPI services running and exposing `/metrics` endpoints
- Default service ports:
  - Whisper API: `http://localhost:8000`
  - Kokoro API: `http://localhost:8001`

### Starting the Monitoring Stack

**Windows:**
```batch
start-monitoring.bat
```

**Linux/macOS:**
```bash
chmod +x start-monitoring.sh
./start-monitoring.sh
```

**Manual start:**
```bash
docker-compose up --build -d
```

## Access Points

- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000
  - Username: `admin`
  - Password: `grafana`

## Configuration

### Prometheus Configuration
The `prometheus.yml` is configured to scrape metrics from:
- Whisper API (`host.docker.internal:8000/metrics`)
- Kokoro API (`host.docker.internal:8001/metrics`)
- Prometheus itself (`localhost:9090`)

### Grafana Setup
Pre-configured with:
- Prometheus datasource
- Whisper API performance dashboard
- Automatic provisioning of dashboards and datasources

## Directory Structure

```
Monitoring_Stack/
├── docker-compose.yml          # Main orchestration file
├── prometheus.yml             # Prometheus configuration
├── start-monitoring.bat       # Windows startup script
├── start-monitoring.sh        # Unix startup script
├── endpoints.yaml            # Legacy endpoint configuration
├── generate_prometheus.py    # Legacy config generator
└── grafana/
    ├── dashboards/
    │   └── whisper-dashboard.json
    └── provisioning/
        ├── dashboards/
        │   └── dashboard.yml
        └── datasources/
            └── prometheus.yml
```

## Adding New Services

1. Update `prometheus.yml` to add new scrape targets
2. Create or import dashboards for new services in Grafana
3. Restart the monitoring stack: `docker-compose restart`

## Legacy Configuration (Optional)

For dynamic endpoint configuration:

1. **Edit Endpoints**
   - Open `endpoints.yaml` and add service endpoints

2. **Generate Config**
   ```bash
   python generate_prometheus.py
   ```

3. **Restart Services**
   ```bash
   docker-compose restart prometheus
   ```

## Troubleshooting

- Ensure FastAPI services expose `/metrics` endpoints
- Check service ports match the Prometheus configuration
- Verify Docker network connectivity between containers
- Check logs: `docker-compose logs prometheus` or `docker-compose logs grafana`
