from django import forms
from django.utils.translation import gettext as _
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import ButtonHolder, Submit, Field
from allauth.account.forms import LoginForm
from crispy_bootstrap5.bootstrap5 import FloatingField


class LoginForm(LoginForm):
    # login = forms.CharField(max_length=30, help_text=_("User name"))
    # password = forms.CharField(max_length=30, widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "login-form-class"
        self.helper.form_id = "login-form"
        self.helper.layout = Layout(
            FloatingField("login"),
            FloatingField("password"),
            Field("remember"),
            ButtonHolder(Submit("submit", "Login", css_class=""), css_class="d-grid gap-2"),
        )

    # def login(self, *args, **kwargs):
    #     return super(LoginForm, self).login(*args, **kwargs)
