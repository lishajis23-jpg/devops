import os
import random
import time

from prometheus_client import Gauge, Summary, start_http_server

PORT = int(os.getenv("METRICS_PORT", "8000"))
PENDING_MIN = int(os.getenv("PENDING_MIN", "10"))
PENDING_MAX = int(os.getenv("PENDING_MAX", "20"))

total_deliveries = Gauge("total_deliveries", "Total number of deliveries")
pending_deliveries = Gauge("pending_deliveries", "Number of pending deliveries")
on_the_way_deliveries = Gauge("on_the_way_deliveries", "Number of deliveries on the way")
average_delivery_time = Summary("average_delivery_time", "Average delivery time in seconds")


def simulate_delivery():
    pending = random.randint(PENDING_MIN, PENDING_MAX)
    on_the_way = random.randint(5, 20)
    delivered = random.randint(30, 70)
    avg_time = random.uniform(15, 45)
    total = pending + on_the_way + delivered

    total_deliveries.set(total)
    pending_deliveries.set(pending)
    on_the_way_deliveries.set(on_the_way)
    average_delivery_time.observe(avg_time)

    print(f"total={total} pending={pending} on_the_way={on_the_way} avg_time={avg_time:.2f}s", flush=True)


if __name__ == "__main__":
    print(f"Starting metrics server on port {PORT} (pending range {PENDING_MIN}-{PENDING_MAX})", flush=True)
    start_http_server(PORT, addr="0.0.0.0")
    while True:
        simulate_delivery()
        time.sleep(1)
