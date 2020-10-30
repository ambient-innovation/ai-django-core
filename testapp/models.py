from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class MySingleSignalModel(models.Model):
    value = models.PositiveIntegerField(default=0)


@receiver(pre_save, sender=MySingleSignalModel)
def increase_value_no_dispatch_uid(sender, instance, **kwargs):
    instance.value += 1


class MyMultipleSignalModel(models.Model):
    value = models.PositiveIntegerField(default=0)


@receiver(pre_save, sender=MyMultipleSignalModel, dispatch_uid='test.mysinglesignalmodel.increase_value_with_uuid')
def increase_value_with_dispatch_uid(sender, instance, **kwargs):
    instance.value += 1


@receiver(post_save, sender=MyMultipleSignalModel)
def send_email(sender, instance, **kwargs):
    msg = EmailMultiAlternatives('Test Mail', 'I am content',
                                 from_email='test@example.com',
                                 to=['random.dude@example.com'])
    msg.send()
