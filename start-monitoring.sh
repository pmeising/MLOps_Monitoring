#!/bin/bash

echo "🚀 Starting Centralized Monitoring Stack..."
echo ""
echo "This will start Prometheus and Grafana to monitor your FastAPI services."
echo "Make sure your FastAPI services are running on their designated ports:"
echo "   • Whisper API (STT): http://localhost:8000"
echo "   • Kokoro API (TTS): http://localhost:8001"
echo ""

# Build and start all services
docker-compose up --build -d

echo "⏳ Waiting for services to start..."
sleep 30

echo "✅ Monitoring Stack started!"
echo ""
echo "📊 Access your monitoring services:"
echo "   • Prometheus: http://localhost:9090"
echo "   • Grafana: http://localhost:3000 (admin/grafana)"
echo ""
echo "📈 Grafana has been pre-configured with:"
echo "   • Prometheus datasource"
echo "   • Whisper API Performance Dashboard"
echo "   • Auto-discovery of FastAPI metrics endpoints"
echo ""
echo "💡 Make sure your FastAPI services expose /metrics endpoints for monitoring."
