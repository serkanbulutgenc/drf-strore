from django import forms
from django.utils.translation import gettext as _
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import ButtonHolder, Submit, Field


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, help_text=_("User name"))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "login-form-class"
        self.helper.form_id = "login-form"
        self.helper.layout = Layout(
            Field("username"), Field("password"), ButtonHolder(Submit("submit", "Login"))
        )
