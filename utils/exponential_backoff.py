"""
Exponential backoff retry decorator with bounded maximum delay.
"""
import time
from functools import wraps

def retry_with_backoff(max_attempts: int = 3, initial_delay: float = 0.1, backoff_factor: float = 2.0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            delay = initial_delay
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1: raise e
                    time.sleep(delay)
                    delay *= backoff_factor
        return wrapper
    return decorator
