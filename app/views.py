from django.http import HttpResponse
from django.http import JsonResponse


def hello(request):
    return HttpResponse("Hello, Django with Uvicorn!")


def health_check(request):
    return JsonResponse({
        "status_code": 200,
        "detail": "ok",
        "result": "working"
    })