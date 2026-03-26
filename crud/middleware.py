import time

def request_timing_middleware(get_response):
    def middleware(request):
        start_time = time.time()
        res = get_response(request)
        duration = time.time() - start
        print(f"Request to {request.path} took {duration:.2f} to complete with status code {res.status_code}")
        return res
    return middleware