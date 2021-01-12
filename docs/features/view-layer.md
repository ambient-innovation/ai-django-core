# View layer

## Introduction

If you are using django in a fullstack way, meaning with django views and templates, you surely
want to use this extra requirement.

Just install the package like this:

``pip install ai-django-core[view-layer]``

If you are using ``pipenv``, you can add the following line to your `Pipfile`:

``ai-django-core = {extras = ["view-layer"],version = "*"}``

## Forms

### Mixins

// todo tbr

## Formset Views

// todo tbr

## View mixins

### CustomPermissionMixin

If you want to handle some custom permission check for which you cannot use the regular django permissions,
just derive your class-based view from `CustomPermissionMixin` and add the method `validate_permissions()`
with your custom logic. Notice that it has to return a boolean value.

For example, you want to allow only the "owner" of an object to view its detail page:

````
from django.views import generic

class MyModelDetailView(CustomPermissionMixin, generics.DetailView):
    ...

        def validate_permissions(self):
            object = super().get_object()
            if self.request.user.employee:
                return False
            return True
````

If the method returns `False`, the regular dispatch will just simply render your `403` page and skip all the other
things within the view.


### RequestInFormKwargsMixin

The ``RequestInFormKwargsMixin`` is a handy helper for passing the request automated form the view to the form. If you
need for example the current request user within the form, you need to have the current request available.

Just add the mixin to the parents of your class-based view class:

````
from django.views import generic

class MyModelEditView(RequestInFormKwargsMixin, generic.CreateView):
    model = MyModel
    template_name = 'myapp/mymodel_edit.html'
    form_class = MyModelForm
    ...

class MyModelEditView(RequestInFormKwargsMixin, generic.UpdateView):
    model = MyModel
    template_name = 'myapp/mymodel_edit.html'
    form_class = MyModelForm
    ...
````

Make sure that you overwrite the ``__init__`` method of your form and move the `request` to the class. Otherwise
the ``super()`` will detect an unrecognised parameter within the kwargs and raise an error:

````
from django.forms.models import ModelForm

class MyModelForm(ModelForm):

    def __init__(self, *args, **kwargs):

        # Get request from kwargs
        self.request = kwargs.pop('request', None)

        # Call the parent method
        super().__init__(*args, **kwargs)

````

That's it.
