# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CreatedAtInfo(models.Model):
    created_at = models.DateTimeField(_(u"Erstellt am"), default=now, db_index=True)

    def save(self, *args, **kwargs):
        # just a fallback for old data
        if not self.created_at:
            self.created_at = now()
        super(CreatedAtInfo, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class CommonInfo(CreatedAtInfo, models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"Erstellt von"), blank=True, null=True,
                                   related_name="%(app_label)s_%(class)s_created", on_delete=models.SET_NULL)
    lastmodified_at = models.DateTimeField(_(u"Zuletzt geändert am"), default=now, db_index=True)
    lastmodified_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"Zuletzt geändert von"), blank=True,
                                        null=True, related_name="%(app_label)s_%(class)s_lastmodified",
                                        on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        self.lastmodified_at = now()
        super(CommonInfo, self).save(*args, **kwargs)

    class Meta:
        abstract = True