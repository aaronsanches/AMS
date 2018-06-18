import time

from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import get_template

from .models import Attendance


@receiver(post_save, sender=Attendance, dispatch_uid=str(time.time()))
def notify(created, **kwargs):
    if created:
        html_template = get_template('attendance_email.html')
        text_template = get_template('attendance_text.txt')
        context = {'when': kwargs.get('instance').when,
                   'subject': kwargs.get('instance').subject, }
        html_alternative = html_template.render(context)
        text_alternative = text_template.render(context)
        from_mail = 'from@eg.com'
        to_mail = 'dindu@mailinator.com'
        msg = EmailMultiAlternatives('Attendance marked', text_alternative,
                                     from_mail, [to_mail])
        msg.attach_alternative(html_alternative, "text/html")
        print(kwargs.get('instance').when)
        msg.send(fail_silently=False)
