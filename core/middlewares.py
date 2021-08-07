import time


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        deviation = time.time() - start
        print(f'Request for url "{request.path}" was processed: {round(deviation, 2)}s.')
        return response
