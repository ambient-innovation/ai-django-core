# View mixins

## CustomPermissionMixin

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
