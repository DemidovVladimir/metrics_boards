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
* Microservice (flask microservice) `http://<host-ip>:5000` and metrics are here `http://<host-ip>:5000/metrics`

To run the entire stack one can use Tilt in order to make it faster:
* Install Tilt: https://docs.tilt.dev/install.html
* Run: cp ./.env_template ./.env
* Input values like repo tocken and repo project id in the newly created .env file
* Run it with: tilt up
* You're goot to go, don't forget to press enter inm your terminal window, read logs from tilt!
* Wait until services are running and then you can visit:

http://localhost:3000 - Grafana
http://localhost:9090 - Prometheus
http://localhost:5000 - Your service metrics as a list
http://localhost:5000/metrics - All available metrics scraped from your service

To run the entire stack one can use Docker-compose that is a bit long:
* Run: cp ./.env_template ./.env
* Input values like repo tocken and repo project id in the newly created .env file
* Run it with: docker-compose up -b
* You're goot to go, don't forget to press enter inm your terminal window, read logs from tilt!
* Wait until services are running and then you can visit:

http://localhost:3000 - Grafana
http://localhost:9090 - Prometheus
http://localhost:5000 - Your service metrics as a list
http://localhost:5000/metrics - All available metrics scraped from your service
