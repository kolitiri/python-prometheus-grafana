# python-prometheus-grafana

This is starting point for putting together the three technologies.

## Architecture

Nothing special. A python application that exposes some Prometheus metrics which are projected in a Grafana dashboard.

### Python app

A python application that uses the [prometheus-client](https://github.com/prometheus/client_python) library to expose a few basic Prometheus metrics at http://localhost:8000.

### Prometheus

A Prometheus instance that is running in a docker container and is configured to scrape the python application which is running on the host.

Look at `prometheus.yml` for the scraping configuration and visit the graph endpoint at http://localhost:9090.

### Grafana

A Grafana instance that is running in a docker container and collects the metrics from Prometheus.

There is a preloaded dashboard (`python-app-dashboard.json`) with some basic graphs to help you get started.

Login to http://localhost:3000 (username=admin, password=admin).

Dashboard "Python App Metrics" should be located inside the General folder.

## Usage

Make sure you have poetry installed.

Start Prometheus and Grafana using `docker-compose` in the root directory.

```
docker-compose up -d
```

Run the python application using poetry.

```
cd python_app/
poetry install
poetry run python python_app/main.py
```

Go to Grafana and view the graphs in the "Python App Metrics" dashboard.

Use `docker-compose` to delete the docker containers and the docker volumes.

```
docker-compose down -v
```

## Authors

Christos Liontos
