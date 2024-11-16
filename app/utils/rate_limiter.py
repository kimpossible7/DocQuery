from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import Response
from time import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, rate_limit_per_minute):
        self.rate_limit_per_minute = rate_limit_per_minute
        self.requests = defaultdict(list)

    def __call__(self, request: Request):
        user_ip = request.client.host
        current_time = time()
        request_times = self.requests[user_ip]

        # Filter requests in the last minute
        self.requests[user_ip] = [t for t in request_times if current_time - t < 60]

        if len(self.requests[user_ip]) >= self.rate_limit_per_minute:
            raise HTTPException(status_code=429, detail="Rate limit exceeded.")

        # Add the current request
        self.requests[user_ip].append(current_time)

rate_limiter = RateLimiter(rate_limit_per_minute=60)
