from django.shortcuts import redirect, render


class _FormsetMixin(object):
    """
    Do NOT use directly. Do use FormsetUpdateViewMixin or FormsetCreateViewMixin
    """
    def get_formset_kwargs(self):
        # may be overridden or extended
        return dict(instance=self.object)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = self.formset_class(**self.get_formset_kwargs())
        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = form_class(**self.get_form_kwargs())
        formset = self.formset_class(request.POST, request.FILES, **self.get_formset_kwargs())

        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()

            if hasattr(self, 'additional_is_valid'):
                self.additional_is_valid(form, formset)

            return redirect(self.get_success_url())
        # Get all context data
        context = self.get_context_data()
        # Update form and formset variables
        context['form'] = form
        context['formset'] = formset
        # Pass all data to template
        return render(request, self.get_template_names(), context)


class FormsetUpdateViewMixin(_FormsetMixin):
    """
    Can be used to validate and save a formset.
    Usage is similar to regular UpdateView:

    class MandantSettingsUpdate(FormsetUpdateViewMixin, generic.UpdateView):
        form_class = MandantSettingsForm
        template_name = 'mandant/mandantsettings_form.html'
        formset_class = inlineformset_factory(Mandant, MandantProdukttyp, form=MandantProdukttypForm, extra=0, \
                                              can_delete=False)
        model = Mandant
        success_url = reverse_lazy('mandant:edit-settings')

        def additional_is_valid(self, form, formset):
            messages.add_message(self.request, messages.INFO, 'Einstellungen wurden erfolgreich aktualisiert.')

    """

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)


class FormsetCreateViewMixin(_FormsetMixin):
    """
    Can be used to validate and save a formset.
    Usage is similar to regular CreateView. See FormsetUpdateViewMixin.
    """

    def post(self, request, *args, **kwargs):
        self.object = None
        return super().post(request, *args, **kwargs)
