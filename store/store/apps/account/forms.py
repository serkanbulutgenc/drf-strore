from django import forms
from django.utils.translation import gettext as _
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import ButtonHolder, Submit, Field, Hidden
from allauth.account.forms import LoginForm, SignupForm
from crispy_bootstrap5.bootstrap5 import FloatingField
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME


class CustomLoginForm(LoginForm):
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
            Hidden(
                REDIRECT_FIELD_NAME,
                value=self.request.GET.get("next") or settings.LOGIN_REDIRECT_URL,
            ),
            ButtonHolder(Submit("submit", "Login", css_class=""), css_class="d-grid gap-2"),
        )

    # def login(self, *args, **kwargs):
    #     if self.user is not None:
    #         return redirect(settings.LOGIN_REDIRECT_URL)
    #     return super(LoginForm, self).login(*args, **kwargs)


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            FloatingField("username"),
            FloatingField("email"),
            FloatingField("password1"),
            FloatingField("password2"),
            ButtonHolder(Submit("sign_up", value="Sign Up")),
        )
