# OpenTelemetry Collector Test Suite

A Dockerized OpenTelemetry Collector test environment for integration testing, specifically designed for testing with Instana plugins and other telemetry systems.

## Features

- 🐳 **Docker/Podman Support**: Run collector in containerized environment
- ⚙️ **Configurable**: Environment-based configuration for ports and settings
- 📊 **Multiple Exporters**: File, logging, and Prometheus exporters for verification
- 🔧 **Test Profiles**: Pre-configured profiles for different test scenarios
- 🚀 **Easy Scripts**: Simple startup, verification, and cleanup scripts

## Quick Start

1. **Clone and setup:**
   ```bash
   git clone https://github.com/laplaque/opentelemetry-collector.git opentelemetry-collector-testsuite
   cd opentelemetry-collector-testsuite
   ```

2. **Start the test collector:**
   ```bash
   chmod +x scripts/*.sh
   ./scripts/start-test-collector.sh
   ```

3. **Send test data to the collector:**
   ```bash
   # gRPC endpoint: localhost:4317
   # HTTP endpoint: localhost:4318
   ```

4. **Verify metrics collection:**
   ```bash
   python3 scripts/verify-metrics.py
   ```

5. **Cleanup:**
   ```bash
   ./scripts/cleanup.sh
   ```

## Configuration

### Environment Variables

Edit `.env` file to customize:

```env
# Protocol Configuration
OTLP_GRPC_PORT=4317
OTLP_HTTP_PORT=4318
PROMETHEUS_EXPORT_PORT=8889
HEALTH_CHECK_PORT=13133

# Output Configuration
OUTPUT_DIR=./test-output
LOG_LEVEL=info

# TLS Configuration (optional)
TLS_CERT_FILE=
TLS_KEY_FILE=

# Forward Configuration (optional)
FORWARD_ENDPOINT=
FORWARD_INSECURE=true
```

### Test Profiles

Located in `profiles/` directory:

- **`instana.yaml`**: Instana-specific configuration with custom attributes
- **`custom-ports.yaml`**: Alternative port configuration for conflict resolution

## Usage with Instana Plugins

This test suite is specifically designed to work with the `instana_plugins` project:

```bash
# From your instana_plugins project
cd /path/to/instana_plugins

# Start the test collector
cd ../opentelemetry-collector-testsuite
./scripts/start-test-collector.sh

# Run your Instana plugin tests
cd ../instana_plugins
python -m pytest tests/test_otel_connector.py

# Verify data collection
cd ../opentelemetry-collector-testsuite
python3 scripts/verify-metrics.py
```

## Docker Commands

### Using Docker Compose
```bash
docker-compose up -d    # Start
docker-compose logs     # View logs
docker-compose down     # Stop
```

### Using Podman Compose
```bash
./scripts/start-test-collector.sh podman    # Start with podman
./scripts/cleanup.sh podman                 # Stop with podman
```

## Output Verification

The collector exports data to multiple targets:

1. **File Export**: `test-output/metrics.json` - JSON format for automated verification
2. **Console Logs**: Docker logs show real-time data flow
3. **Prometheus Metrics**: `http://localhost:8889/metrics` for manual inspection
4. **Health Check**: `http://localhost:13133` for service status

## Testing Different Scenarios

### Custom Port Testing
```bash
# Edit .env to use different ports
OTLP_GRPC_PORT=9317
OTLP_HTTP_PORT=9318

# Restart collector
./scripts/cleanup.sh
./scripts/start-test-collector.sh
```

### TLS Testing
```bash
# Add certificate paths to .env
TLS_CERT_FILE=/path/to/cert.pem
TLS_KEY_FILE=/path/to/key.pem

# Restart with TLS enabled
./scripts/cleanup.sh
./scripts/start-test-collector.sh
```

### Forwarding to Real Backend
```bash
# Configure forwarding in .env
FORWARD_ENDPOINT=https://your-otel-backend:4317
FORWARD_INSECURE=false

# Restart collector
./scripts/cleanup.sh
./scripts/start-test-collector.sh
```

## Troubleshooting

### Port Conflicts
If ports are already in use, modify `.env` file:
```env
OTLP_GRPC_PORT=14317
OTLP_HTTP_PORT=14318
PROMETHEUS_EXPORT_PORT=18889
HEALTH_CHECK_PORT=23133
```

### Permission Issues
Make scripts executable:
```bash
chmod +x scripts/*.sh
```

### Docker Issues
Check Docker/Podman status:
```bash
docker --version
docker-compose --version
# or
podman --version
podman-compose --version
```

## Integration with CI/CD

Example GitHub Actions workflow:

```yaml
- name: Start OpenTelemetry Test Collector
  run: |
    cd opentelemetry-collector-testsuite
    ./scripts/start-test-collector.sh
    
- name: Run Integration Tests
  run: |
    # Your test commands here
    
- name: Verify Telemetry Data
  run: |
    cd opentelemetry-collector-testsuite
    python3 scripts/verify-metrics.py
    
- name: Cleanup
  run: |
    cd opentelemetry-collector-testsuite
    ./scripts/cleanup.sh
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Add tests for new functionality
4. Update documentation
5. Submit a pull request

## License

This project inherits the license from the upstream OpenTelemetry Collector project.
