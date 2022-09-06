from django.core.mail import send_mail


def send_mail_to(subject, message, receivers):
    send_mail(subject,
              message,
              'jeeshma@sayonetech.com',
              [
                  receivers,  # add more emails to this list of you want to
              ],
              fail_silently=False,
              )
