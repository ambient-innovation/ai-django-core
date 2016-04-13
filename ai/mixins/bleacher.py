import bleach


class BleacherMixin(object):

    def __init__(self, *args, **kwargs):
        super(BleacherMixin, self).__init__(*args, **kwargs)
        self.fields_to_bleach = getattr(self, 'BLEACH_FIELD_LIST', [])
        self.allowed_tags = getattr(self, 'ALLOWED_TAGS',
                               bleach.ALLOWED_TAGS + ['span', 'p', 'h1', 'h2', 'h3', 'h4', 'img', 'div'])

        standard_allowed_attributes = {
            '*': ['class', 'style', 'id'],
            'a': ['href', 'rel'],
            'img': ['alt', 'src'],
        }

        self.allowed_attributes = getattr(self, 'ALLOWED_ATTRIBUTES', standard_allowed_attributes)

    def save(self, *args, **kwargs):
        for field in self.fields_to_bleach:
            str_to_bleach = getattr(self, 'field', "")
        bleach.clean(str_to_bleach, tags=self.allowed_tags, attributes=self.allowed_attributes)

        super(BleacherMixin, self).save(*args, **kwargs)
