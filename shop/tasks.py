from celery import shared_task
from django.core import mail
from django.template.loader import get_template
from elektroswit.settings import EMAIL_HOST_USER


@shared_task
def message_send(context, order):
    connection = mail.get_connection()
    email1 = mail.EmailMessage(
        'ELEKTROSWIT: Спасибо за покупку!',
        ''.join(str(get_template('mail_order_usr/index.html').render(context))),
        EMAIL_HOST_USER,
        [order.email],
        connection=connection
    )
    context['to_admin'] = True
    context['email'] = order.email
    context['message'] = order.message
    context['phone'] = order.phone
    email2 = mail.EmailMessage(
        'ELEKTROSWIT: Поступил новый заказ!',
        ''.join(str(get_template('mail_order_usr/index.html').render(context))),
        EMAIL_HOST_USER,
        ['saninstein@yandex.ua'],
        connection=connection
    )
    email1.content_subtype = 'html'
    email2.content_subtype = 'html'
    email1.send(fail_silently=True)
    email2.send(fail_silently=True)
    connection.close()
    print('in')
    return 'OK'


