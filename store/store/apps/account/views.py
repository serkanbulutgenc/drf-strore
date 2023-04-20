from django.shortcuts import render
from django.views import generic
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.conf import settings


class LoginView(generic.FormView):
    form_class = LoginForm
    success_url = "/products/"
    template_name = "account/login.html"

    def post(self, request, *args, **kwargs) -> HttpResponse:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse("product-web:list"))
        else:
            return redirect(reverse("account:login"))
        # return super().post(request, *args, **kwargs)


class LogoutView(LoginRequiredMixin, generic.RedirectView):
    url = settings.LOGIN_URL

    def get(self, request, *args, **kwargs) -> HttpResponse:
        logout(request)
        return super().get(request, *args, **kwargs)


# Create your views here.
