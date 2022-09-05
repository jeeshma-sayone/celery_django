from celery import shared_task
from django.core.mail import send_mail

from time import sleep


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_email_task():
    print("====== START ======")
    # sleep(10)
    # send_mail('Celery Task Worked!',
    #           'This is proof the task worked!',
    #           'jeeshma@sayonetech.com',
    #           ['jeeshma2009@gmail.com'])

    send_mail('Celery Task TEST!',
              'This is proof the task worked!',
              'jeeshma@sayonetech.com',
              [
                  'jeeshma2009@gmail.com',  # add more emails to this list of you want to
              ],
              fail_silently=False,
              )
    print("====== FINISH ======")

    return None


@shared_task(bind=True)
def test_func(self):
    # operations
    for i in range(10):
        print(i)
    return "Done"
