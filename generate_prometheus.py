import yaml

# Load endpoints configuration
with open('endpoints.yaml', 'r') as f:
    config = yaml.safe_load(f)
    endpoints = config['endpoints']

# Group endpoints by service type based on name patterns
fastapi_services = []
mlflow_training_services = []
mlflow_server_services = []
other_services = []

for ep in endpoints:
    target = f"{ep['ip']}:{ep['port']}"
    name = ep['name'].lower()
    service_type = ep.get('service_type', '').lower()
    
    # Categorize services based on service_type or name patterns
    if service_type == 'mlflow_server' or name == 'mlflow_server':
        mlflow_server_services.append(target)
    elif service_type == 'mlflow_training' or 'training' in name:
        mlflow_training_services.append(target)
    elif service_type == 'fastapi' or name in ['stt', 'tts', 'llm', 'whisper', 'kokoro', 'liquidai']:
        fastapi_services.append(target)
    else:
        other_services.append(target)

# Build scrape configs
scrape_configs = []

# FastAPI services job (main AI services)
if fastapi_services:
    scrape_configs.append({
        'job_name': 'fastapi_services',
        'static_configs': [
            {'targets': fastapi_services}
        ]
    })

# MLFlow training job
if mlflow_training_services:
    scrape_configs.append({
        'job_name': 'mlflow_training',
        'static_configs': [
            {'targets': mlflow_training_services}
        ],
        'scrape_interval': '30s'
    })

# MLFlow server job
if mlflow_server_services:
    scrape_configs.append({
        'job_name': 'mlflow_server',
        'static_configs': [
            {'targets': mlflow_server_services}
        ],
        'metrics_path': '/metrics',
        'scrape_interval': '60s'
    })

# Other services (if any)
if other_services:
    scrape_configs.append({
        'job_name': 'other_services',
        'static_configs': [
            {'targets': other_services}
        ]
    })

# Create the final prometheus configuration
prometheus_config = {
    'global': {
        'scrape_interval': '15s'
    },
    'scrape_configs': scrape_configs
}

# Write to prometheus.yml with proper formatting
with open('prometheus.yml', 'w') as f:
    yaml.dump(prometheus_config, f, default_flow_style=False, sort_keys=False)

print('prometheus.yml generated successfully.')
print(f'Generated {len(scrape_configs)} job(s):')
for config in scrape_configs:
    targets = config['static_configs'][0]['targets']
    print(f"  - {config['job_name']}: {len(targets)} target(s)")
    for target in targets:
        print(f"    • {target}")
