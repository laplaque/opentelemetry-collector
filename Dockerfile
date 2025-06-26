FROM otel/opentelemetry-collector:latest

COPY config.yaml /etc/otelcol/config.yaml
