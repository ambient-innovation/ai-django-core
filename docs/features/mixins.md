# Mixins

## BleacherMixin

### Motivation

Sometimes it is necessary to allow the user to write HTML and save this in the database. Unfortunately this creates the
possibility to insert malicious content. A package called [bleach](https://pypi.org/project/bleach) can help with this
problem.

Keep in mind that django templates will automatically escape all HTML and script code it renders. So if you want to
allow the user to create custom HTML content, this content has to be marked as "safe" in the template. This will
deactivate the escaping - and will render every evil piece of code the user inserted (intentionally or not).

If you allow custom content to be rendered "safely", you should whitelist harmless HTML tags and attributes and remove
all possible dangers - and as we are working with django, we want to define this security layer on a single point in the
code to be sure that it won't be forgotten at any time.

### Model mixin

Therefore, we create the `BleacherMixin` which is used in the model like this.

```
class MyModel(BleacherMixin, models.Model):
    BLEACH_FIELD_LIST = ['my_html_field']

    my_field = models.IntegerField()
    my_html_field = models.TextField()
```

This will automatically bleach (meaning escape) all non-whitelisted HTML tags and attributes in the defined fields while
leaving the white-listed ones intact.

Technically the mixin bleaches the field on a model `safe()` call.

### Default settings

The default settings are as follows:

```
DEFAULT_ALLOWED_ATTRIBUTES = {
    '*': ['class', 'style', 'id'],
    'a': ['href', 'rel'],
    'img': ['alt', 'src'],
}

DEFAULT_ALLOWED_TAGS = bleach.ALLOWED_TAGS + ['span', 'p', 'h1', 'h2', 'h3', 'h4', 'h5',*
                                              'h6', 'img', 'div', 'u', 'br', 'blockquote']
```

### Customize whitelists

If you want to alter your whitelists, just add something similar to this in your global django `settings.py`:

```
# Bleach
BLEACH_ALLOWED_ATTRIBUTES = {
    '*': ['class', 'style', 'id'],
    'a': ['href', 'rel', 'target'],
    'img': ['alt', 'src'],
}

BLEACH_ALLOWED_TAGS = ['span', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                       'img', 'div', 'u', 'br', 'blockquote', 'strong', 'a']

```

### Limitations

As the mixin works by extending the models `safe()`-method, bleaching **will not** be applied on all storage operations
done directly by the database, like `MyModel.objects.all().update(my_html_field='I am malicious content!')`.

## Validation

### CleanOnSaveMixin

If you are following the fat-model approach, it might be convenient to put some low-level validation in the models "
clean" method which will be automatically called when using forms (or therefore, django admin). Unfortunately, it is not
called on a regular model save. Just derive your model from the `CleanOnSaveMixin` mixin and your clean will be called
on every save. Note that it won't be called on bulk operations not targeting model save.

````python
class ModelWithCleanMixin(CleanOnSaveMixin, models.Model):
    def clean(self):
        # to your magic here
````
