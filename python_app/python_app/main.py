import random
import time

from prometheus_client import (
	start_http_server,
	Summary,
)


PROMETHEUS_PORT = 8000

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary(
	'request_processing_seconds',
	'Time spent processing request'
)

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(PROMETHEUS_PORT)

    print(f"Exposing Prometheus metrics at: http://localhost:{PROMETHEUS_PORT}/metrics")

    # Generate some requests.
    while True:
        process_request(random.random())
