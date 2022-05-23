from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from ai_django_core.managers import GloballyVisibleQuerySet
from ai_django_core.mixins.validation import CleanOnSaveMixin
from ai_django_core.models import CommonInfo


class MySingleSignalModel(models.Model):
    value = models.PositiveIntegerField(default=0)

    objects = GloballyVisibleQuerySet.as_manager()


class ForeignKeyRelatedModel(models.Model):
    single_signal = models.ForeignKey(
        MySingleSignalModel, on_delete=models.CASCADE, related_name='foreign_key_related_models'
    )

    objects = GloballyVisibleQuerySet.as_manager()


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
    msg = EmailMultiAlternatives(
        'Test Mail', 'I am content', from_email='test@example.com', to=['random.dude@example.com']
    )
    msg.send()


class CommonInfoBasedModel(CommonInfo):
    value = models.PositiveIntegerField(default=0)


class ModelWithFkToSelf(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)


class ModelWithOneToOneToSelf(models.Model):
    peer = models.OneToOneField('self', blank=True, null=True, related_name='related_peer', on_delete=models.CASCADE)


class ModelWithCleanMixin(CleanOnSaveMixin, models.Model):
    def clean(self):
        return True
