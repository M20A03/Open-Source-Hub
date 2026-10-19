"""
SHA-256 and MD5 cryptographic hashing helpers.
"""
import hashlib

def sha256_digest(data: str) -> str:
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def md5_digest(data: str) -> str:
    return hashlib.md5(data.encode('utf-8')).hexdigest()
