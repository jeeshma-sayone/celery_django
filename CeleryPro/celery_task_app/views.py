from django.http import HttpResponse
from django.shortcuts import render
from .tasks import sleepy, send_email_task, test_func


# Create your views here.
def index(request):
    send_email_task.delay()
    # send_email_task()
    return HttpResponse('<h1>EMAIL HAS BEEN SENT WITH CELERY!</h1>')


def test(request):
    test_func.delay()
    return HttpResponse("Done")