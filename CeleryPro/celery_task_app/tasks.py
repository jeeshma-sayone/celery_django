import celery
from celery import shared_task
from celery.app import task
from django.core.mail import send_mail

from time import sleep

from celery_task_app.inform_using_mail import send_mail_to


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


# @shared_task(bind=True
@shared_task
def send_email_task():
    print("====== START ====== BEAT")
    # sleep(10)
    # send_mail('Celery Task Worked!',
    #           'This is proof the task worked!',
    #           'jeeshma@sayonetech.com',
    #           ['jeeshma2009@gmail.com'])

    send_mail('Celery Beat Task TEST!',
              'This is proof the task worked!',
              'jeeshma@sayonetech.com',
              [
                  'jeeshma2009@gmail.com',  # add more emails to this list of you want to
              ],
              fail_silently=False,
              )
    print("====== FINISH ======")

    return None
#
#
# @shared_task(bind=True)
# def test_func(self):
#     # operations
#     for i in range(10):
#         print(i)
#     return "Done"


@shared_task(bind=True)
def my_first_task(self):
    print("=== start ===")
    subject = 'Celery Task TEST!'
    message = 'My task done successfully'
    receivers = 'jeeshma2009@gmail.com'
    is_task_completed = False
    error = ''
    try:
        sleep(5)
        is_task_completed = True
    except Exception as err:
        error = str(err)
        print("err!!!!!!!!!!!!", err)
    if is_task_completed:
        send_mail_to(subject, message, receivers)
        return 'first_task_done'
    else:
        send_mail_to(subject, error, receivers)
        return str(error)
    # print("=== end ===")

