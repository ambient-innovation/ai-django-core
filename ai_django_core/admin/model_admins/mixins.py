from django.urls import resolve


class AdminCreateFormMixin:
    """
    Mixin to easily use a different form for the create case (in comparison to "edit") in the django admin
    Logic copied from `django.contrib.auth.admin.UserAdmin`
    """
    add_form = None

    def get_form(self, request, obj=None, **kwargs):
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)


class AdminNoInlinesForCreateMixin:
    """
    Avoid showing any inline admins when being in the create case of a record
    """

    def get_inline_instances(self, request, obj=None):
        if obj is None:
            return []
        return super().get_inline_instances(request, obj)


class AdminRequestInFormMixin:
    """
    Mixin to add the current request to a form used in the django admin
    """

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.request = request
        return form


class FetchParentObjectInlineMixin:
    """
    Fetches the parent object via the URL resolver and makes it available throughout the entire class.
    Attention: Use only in inline admin classes.
    """
    parent_object = None

    @staticmethod
    def _resolve_url(request):
        return resolve(request.path_info)

    def get_parent_object_from_request(self, request):
        resolved = self._resolve_url(request)
        if resolved.kwargs:
            return self.parent_model.objects.get(pk=resolved.kwargs.get('object_id', None))
        return None

    def get_formset(self, request, obj=None, **kwargs):
        # Fetch parent object - cannot be done in the init method because request is not available there
        self.parent_object = self.get_parent_object_from_request(request)
        return super().get_formset(request, obj, **kwargs)


class FetchObjectMixin:
    """
    Fetches the current object via the URL resolver and makes it available throughout the entire class.
    """

    def get_object_from_request(self, request):
        resolved = resolve(request.path_info)
        if resolved.kwargs:
            return self.model.objects.get(pk=resolved.kwargs.get('object_id', None))
        return None


class CommonInfoAdminMixin:
    """
    Mixin to be used in a django model admin class.
    Sets all four `CommonInfo` attributes to "readonly" and sets the creator / last modifier on form save.
    """

    def get_readonly_fields(self, request, obj=None):
        return super().get_readonly_fields(request, obj) + ('created_by', 'lastmodified_by', 'created_at',
                                                            'lastmodified_at')

    def save_form(self, request, form, change):
        if form.instance and request.user:
            if not form.instance.id:
                form.instance.created_by = request.user
            form.instance.lastmodified_by = request.user

        return super().save_form(request, form, change)
