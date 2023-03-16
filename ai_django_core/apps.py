from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AmbientToolboxConfig(AppConfig):
    name = 'ai_django_core'
    verbose_name = _('Ambient Toolbox')
