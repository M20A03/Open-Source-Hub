"""
Common validation utilities for email and alphanumeric formats.
"""
import re

def is_valid_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def is_alphanumeric(text: str) -> bool:
    return text.isalnum()
