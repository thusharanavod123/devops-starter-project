"""Prometheus metrics utilities."""
from functools import wraps
from flask import request
from prometheus_client import Counter, Histogram
import time

# Define metrics
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['method', 'endpoint']
)


def request_counter(f):
    """Decorator to count requests.
    
    Args:
        f: Function to decorate
        
    Returns:
        Wrapped function
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        response = f(*args, **kwargs)
        status = response[1] if isinstance(response, tuple) else 200
        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.endpoint,
            status=status
        ).inc()
        return response
    return decorated_function


def request_duration(f):
    """Decorator to measure request duration.
    
    Args:
        f: Function to decorate
        
    Returns:
        Wrapped function
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        start_time = time.time()
        response = f(*args, **kwargs)
        duration = time.time() - start_time
        REQUEST_LATENCY.labels(
            method=request.method,
            endpoint=request.endpoint
        ).observe(duration)
        return response
    return decorated_function
