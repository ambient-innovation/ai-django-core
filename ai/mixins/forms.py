# coding=utf-8
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.utils.translation import ugettext_lazy as _

__author__ = 'dennismosemann'


class RequestInFormKwargsMixin(object):
    """
    Injects the request in the form.
    Attention: Have to be removed in the init of the form
    """
    def get_form_kwargs(self):
        kwargs = super(RequestInFormKwargsMixin, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class CrispyLayoutFormMixin(object):
    """
    Styles the form in bootstrap style
    """
    def __init__(self, *args, **kwargs):
        # Crispy
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal form-bordered form-row-stripped'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', _(u'Speichern')))
        self.helper.form_tag = True
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.label_size = ' col-md-offset-3'

        super(CrispyLayoutFormMixin, self).__init__(*args, **kwargs)