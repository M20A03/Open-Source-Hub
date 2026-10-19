"""
Unit test suite for Token Bucket rate limiter.
"""
from utils.rate_limiter import TokenBucket

def test_token_bucket():
    tb = TokenBucket(2, 1.0)
    assert tb.allow_request() is True; assert tb.allow_request() is True
