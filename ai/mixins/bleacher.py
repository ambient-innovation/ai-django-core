import bleach


class BleacherMixin(object):
    DEFAULT_ALLOWED_ATTRIBUTES = {
        '*': ['class', 'style', 'id'],
        'a': ['href', 'rel'],
        'img': ['alt', 'src'],
    }

    DEFAULT_ALLOWED_TAGS = bleach.ALLOWED_TAGS + ['span', 'p', 'h1', 'h2', 'h3', 'h4', 'h5',
                                                  'h6', 'img', 'div', 'u', 'br', 'blockquote']

    def __init__(self, *args, **kwargs):
        super(BleacherMixin, self).__init__(*args, **kwargs)
        self.fields_to_bleach = getattr(self, 'BLEACH_FIELD_LIST', [])
        self.allowed_tags = getattr(self, 'ALLOWED_TAGS', self.DEFAULT_ALLOWED_TAGS)
        self.allowed_attributes = getattr(self, 'ALLOWED_ATTRIBUTES', self.DEFAULT_ALLOWED_ATTRIBUTES)

    def _bleach_field(self, field_name):
        str_to_bleach = getattr(self, field_name, "")
        cleaned_value = bleach.clean(str_to_bleach, tags=self.allowed_tags, attributes=self.allowed_attributes)
        setattr(self, field_name, cleaned_value)

    def save(self, *args, **kwargs):
        for field in self.fields_to_bleach:
            self._bleach_field(field)

        super(BleacherMixin, self).save(*args, **kwargs)
