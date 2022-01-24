# View layer

## Introduction

If you are using django in a fullstack way, meaning with django views and templates, you surely want to use this extra
requirement.

Just install the package like this:

``pip install ai-django-core[view-layer]``

If you are using ``pipenv``, you can add the following line to your `Pipfile`:

``ai-django-core = {extras = ["view-layer"],version = "*"}``

## Forms

### CrispyLayoutFormMixin

This neat mixin provides a basic setup to turn a regular Django form into a nice bootstrapy crispy form.

````
class MyForm(CrispyLayoutFormMixin, forms.Form):
    pass
````

The form will have the following properties:

| Attribute     | Default configuration                           |
| ------------- | ----------------------------------------------- |
| Form tag      | Yes                                             |
| Form class    | form-horizontal form-bordered form-row-stripped |
| Method        | POST                                            |
| Submit button | Set, called "Save"                              |
| Label class   | col-md-3                                        |
| Field class   | col-md-9                                        |
| Label size    | col-md-offset-3                                 |

## Formsets

### CountChildrenFormsetMixin

This mixin provides a method which returns the current number of children of this formset. It automatically takes care
of deleted or to-be-deleted children. Have a look at the example use-case below:

````
class DataFieldFormset(CountChildrenFormsetMixin, BaseInlineFormSet):

    def clean(self):
        cleaned_data = super().clean()

        # Count children
        number_of_children = self.get_number_of_children()

        # do some magic

        return cleaned_data
````

Note that the form needs to be validated before you can use this method.

## Formset Views

This package provides two mixins supporting class-based views combined with formsets. The `FormsetCreateViewMixin` is to
be used with a `generic.CreateView`, the `FormsetUpdateViewMixin` together with `generic.UpdateView`.

The idea behind these mixins to make handling formset less pain and provide the comfy feeling you are used from regular
forms.

Here is an example for a create view:

```
class MyModelCreateView(FormsetCreateViewMixin, generic.CreateView):
    model = MyModel
    template_name = 'my_app/my_model_edit.html'
    form_class = MyModelEditForm
    formset_class = inlineformset_factory(MyModel, MyModelChild,
                                          form=MyModelChildForm,
                                          formset=MyModelChildFormset)

    def get_formset_kwargs(self):
        # this is optional!
        kwargs = super().get_formset_kwargs()
        kwargs['request'] = self.request
        return kwargs
```

You just define - similar to the regular form - a `formset_class` as a class attribute. All the required handling like
validation will happen magically. If you need to pass additional values to your formset, just extend the method
`get_formset_kwargs()` as you would for djangos `get_form_kwargs()`.

If you want to update a model and its children, here is an example for the edit-case:

```
class MyModelEditView(FormsetUpdateViewMixin, generic.UpdateView):
    model = MyModel
    template_name = 'my_app/my_model_edit.html'
    form_class = MyModelEditForm
    formset_class = inlineformset_factory(MyModel, MyModelChild,
                                          form=MyModelChildForm,
                                          formset=MyModelChildFormset)

    def get_formset_kwargs(self):
        # this is optional!
        kwargs = super().get_formset_kwargs()
        kwargs['request'] = self.request
        return kwargs
```

## View mixins

### CustomPermissionMixin

If you want to handle some custom permission check for which you cannot use the regular django permissions, just derive
your class-based view from `CustomPermissionMixin` and add the method `validate_permissions()`
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

## Generic views

### ToggleView

Django provides a neat way of enabling the update of a given object through the `generic.UpdateView`. This method will
validate the user data using a given form. But sometimes an update is required which doesn't need any user data being
sent, like toggling a flag or updating a timestamp. For these cases, just use the `ToggleView` - it works basically the
same as the `UpdateView` - except that "POST" is required and that no form has to be defined.

```
from ai_django_core.view_layer.views import ToggleView

class ToggleActiveStateView(ToggleView):
    model = MyModel
    template_name = 'myapp/my_model_edit.html'

    def post(self, request, *args, **kwargs):
        # Update object
        obj = self.get_object()
        obj.is_active = not obj.is_active
        obj.save()

        return render(self.request, self.template_name, {'object': obj})
```
