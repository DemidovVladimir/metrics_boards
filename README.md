Local-docker-prometheus-metrics-monitor
========

A monitoring solution for Docker hosts and containers with [Prometheus](https://prometheus.io/), [Grafana](http://grafana.org/), [cAdvisor](https://github.com/google/cadvisor),
[NodeExporter](https://github.com/prometheus/node_exporter) and alerting with [AlertManager](https://github.com/prometheus/alertmanager).

Containers:
* Microservice (flask service) `http://<host-ip>:5000`
* Prometheus (metrics database) `http://<host-ip>:9090`
* Prometheus-Pushgateway (push acceptor for ephemeral and batch jobs) `http://<host-ip>:9091`
* AlertManager (alerts management) `http://<host-ip>:9093`
* Grafana (visualize metrics) `http://<host-ip>:3000`
* NodeExporter (host metrics collector)
* cAdvisor (containers metrics collector)
* Caddy (reverse proxy and basic auth provider for prometheus and alertmanager)

To start the entire stack you only have to:
* Run: tilt up
* Wait until services are running and then you can visit:

http://localhost:3000 - Grafana
http://localhost:9090 - Prometheus
http://localhost:5000 - Flask based service
http://localhost:5000/metrics - Service metrics titles
