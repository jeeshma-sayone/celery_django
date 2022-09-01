# celery_django

Celery is an open-source Python library which is used to run the tasks asynchronously. It is a task queue that holds the tasks and distributes them to the workers in a proper manner. It is primarily focused on real-time operation but also supports scheduling (run regular interval tasks). It enhances the end's user activity amazingly. Celery introduces the various message brokers such as RabbitMQ and Redis.

Celery combines various web frameworks, including Flask, Pylons, web2py, Tryton, and Tornado.


# Purpose

Suppose we need to access API every minute (hour), or we want to send multiple emails at the end of the day. Celery can schedule that type of periodic task easily.

Let's take another scenario: a user sends a request, and the page is taking too long to load. Meanwhile, Celery decreases page load time by running part of the functionality as postponed tasks on the same server or sometime different server.

Celery's workers can then update the UI via callbacks, process files, send emails, make changes in database and many more.

The main advantage of Celery is that our application can continue to respond to client requests. So the end-users don't have to wait unnecessarily.