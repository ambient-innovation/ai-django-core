from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from .storage import USE_SCANNER
from .scanner import AVScanner

scanner = AVScanner()


def file_validator(f):
    if USE_SCANNER:
        has_virus, name = scanner.has_virus(f.file)
        if has_virus:
            raise ValidationError(_('In dieser Datei wurde ein Virus erkannt.'))
            # raise ValidationError(_('Virus "{}" wurde erkannt.').format(name))


class AVProtectedFileField(models.FileField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(file_validator)


class AVProtectedImageField(models.ImageField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(file_validator)
