import yaml

with open('endpoints.yaml', 'r') as f:
    endpoints = yaml.safe_load(f)['endpoints']

scrape_targets = [f"{ep['ip']}:{ep['port']}" for ep in endpoints]

prometheus_config = {
    'global': {'scrape_interval': '15s'},
    'scrape_configs': [
        {
            'job_name': 'fastapi_services',
            'static_configs': [
                {'targets': scrape_targets}
            ]
        }
    ]
}

with open('prometheus.yml', 'w') as f:
    yaml.dump(prometheus_config, f, default_flow_style=False)
print('prometheus.yml generated successfully.')
