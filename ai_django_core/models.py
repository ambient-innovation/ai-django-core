from django.conf import settings
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from ai_django_core.middleware.current_user import CurrentUserMiddleware


class CreatedAtInfo(models.Model):
    created_at = models.DateTimeField(_("Erstellt am"), default=now, db_index=True)

    def save(self, *args, **kwargs):
        # just a fallback for old data
        if not self.created_at:
            self.created_at = now()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class CommonInfo(CreatedAtInfo, models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Erstellt von"), blank=True, null=True,
                                   related_name="%(app_label)s_%(class)s_created", on_delete=models.SET_NULL)
    lastmodified_at = models.DateTimeField(_("Zuletzt geändert am"), default=now, db_index=True)
    lastmodified_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Zuletzt geändert von"), blank=True,
                                        null=True, related_name="%(app_label)s_%(class)s_lastmodified",
                                        on_delete=models.SET_NULL)

    @staticmethod
    def get_current_user():
        """
        Get the currently logged in user over middleware.
        Can be overwritten to use e.g. other middleware or additional functionality.
        :return: user instance
        """
        return CurrentUserMiddleware.get_current_user()

    def set_user_fields(self, user):
        """
        Set user-related fields before saving the instance.
        If no user with primary key is given the fields are not set.
        :param user: user instance of current user
        """
        if user and user.pk:
            if not self.pk:
                self.created_by = user
            self.lastmodified_by = user

    def save(self, *args, **kwargs):
        self.lastmodified_at = now()
        current_user = self.get_current_user()
        self.set_user_fields(current_user)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
