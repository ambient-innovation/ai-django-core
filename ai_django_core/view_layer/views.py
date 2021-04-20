from django.shortcuts import render
from django.views import generic
from django.views.defaults import ERROR_403_TEMPLATE_NAME


class CustomPermissionMixin(generic.View):
    """
    This mixin provides the method `validate_permissions()` to create a space where custom, non-django-permissions
    can live. This method will be called in the `dispatch()` method to avoid executing unnecessary logic in the
    "permission denied" case.
    """

    def validate_permissions(self) -> bool:
        return True

    def dispatch(self, request, *args, **kwargs):
        if self.validate_permissions():
            return super().dispatch(request, *args, **kwargs)
        else:
            return render(self.request, ERROR_403_TEMPLATE_NAME, status=403)


class RequestInFormKwargsMixin:
    """
    Injects the request in the form.
    Attention: Have to be removed in the init of the form (via .pop())
    """

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs
