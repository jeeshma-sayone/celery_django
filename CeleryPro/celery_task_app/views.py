from django.http import HttpResponse
from django.shortcuts import render
from .tasks import sleepy, my_first_task, send_email_task


# Create your views here.
def index(request):
    my_first_task.delay()
    # send_email_task.delay()
    # send_email_task()
    # my_first_task(5)
    return HttpResponse('<h1>EMAIL HAS BEEN SENT WITH CELERY!</h1>')


# def test(request):
#     test_func.delay()
#     return HttpResponse("Done")
