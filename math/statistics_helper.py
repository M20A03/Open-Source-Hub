"""
Fundamental statistical calculation routines: mean, variance, standard deviation.
"""
import math

def calculate_mean(data: list) -> float:
    return sum(data) / len(data) if data else 0.0

def calculate_variance(data: list) -> float:
    if len(data) <= 1: return 0.0
    m = calculate_mean(data)
    return sum((x - m) ** 2 for x in data) / len(data)

def calculate_std_dev(data: list) -> float:
    return math.sqrt(calculate_variance(data))
