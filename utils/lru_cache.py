"""
Lightweight LRU Cache utility decorator.
"""
from functools import wraps

def simple_lru(maxsize=128):
    def decorator(fn):
        cache = {}
        order = []
        @wraps(fn)
        def wrapper(*args):
            if args in cache:
                order.remove(args)
                order.append(args)
                return cache[args]
            res = fn(*args)
            if len(order) >= maxsize:
                oldest = order.pop(0)
                del cache[oldest]
            cache[args] = res
            order.append(args)
            return res
        return wrapper
    return decorator
