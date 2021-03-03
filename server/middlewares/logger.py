from django.utils.log import log_response


class RequestLoggerMiddleware:
    def __init__(self, view_func):
        self.view_func = view_func

    def __call__(self, request, *args, **kwargs):
        response = self.view_func(request, *args, **kwargs)
        meta = request.META
        log_response(f"user-agent: {meta['HTTP_USER_AGENT']}; path: {request.path}", response=response, request=request)
        return response
