Local-docker-prometheus-metrics-monitor
========

A monitoring solution for Docker hosts and containers with [Prometheus](https://prometheus.io/), [Grafana](http://grafana.org/), [cAdvisor](https://github.com/google/cadvisor),
[NodeExporter](https://github.com/prometheus/node_exporter) and alerting with [AlertManager](https://github.com/prometheus/alertmanager).

Containers:

* Prometheus (metrics database) `http://<host-ip>:9090`
* Prometheus-Pushgateway (push acceptor for ephemeral and batch jobs) `http://<host-ip>:9091`
* AlertManager (alerts management) `http://<host-ip>:9093`
* Grafana (visualize metrics) `http://<host-ip>:3000`
* NodeExporter (host metrics collector)
* cAdvisor (containers metrics collector)
* Caddy (reverse proxy and basic auth provider for prometheus and alertmanager)

Connecting nodejs exporter to Prometheus:

Under dockprom/prometheus/prometheus.yml , you can find an array of jobs prometheus will scrape. Add the following into the list:

```
- job_name: 'nodejs'
  scrape_interval: 10s
  honor_labels: true
  static_configs:
    - targets: ['host.docker.internal:<port>']
```

To validate logs:
* Change if needed Tiltfile to point to your locally (docker) running service
* Run yarn
* Run: tilt up
* Wait until services are running and then you can visit:

http://localhost:3000 - Grafana
http://localhost:9090 - Prometheus
http://localhost:<port> - Your service metrics as a list