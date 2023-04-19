from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import gettext as _
from django.urls import reverse
from store.apps.product.models import Product
from django.contrib import messages
from .forms import ProductForm
from django.views import generic
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ProductList(generic.ListView):
    model = Product
    template_name = "product/list.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["extra"] = "Extra data"
        return context

    def get_queryset(self):
        return Product.active.order_by("-created_at")[:5]


class ProductDetail(generic.DetailView):
    model = Product
    template_name = "product/detail.html"
    context_object_name = "product"


class ProductCreate(SuccessMessageMixin, generic.CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product/update.html"
    success_message = "Form has been saved successfully"
    success_url = "/products/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = "create"
        return context

    def post(self, request, *args, **kwargs) -> HttpResponse:
        return super().post(request, *args, **kwargs)


class ProductUpdate(generic.UpdateView):
    model = Product
    template_name = "product/update.html"
    success_url = "/products/{id}/"
    fields = [
        "title",
        "category",
        "brand",
        "description",
        "original_price",
        "sale_price",
        "is_active",
    ]


def product_list_view(request):
    products = Product.active.all()
    return render(request, "product/list.html", {"products": products})


def product_detail_view(request, pk: int):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product/detail.html", {"product": product})


def product_create_view(request):
    if request.method == "GET":
        p_form = ProductForm()
        return render(request, "product/update.html", {"form": p_form, "action": "create"})
    elif request.method == "POST":
        p_form = ProductForm(request.POST)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, _("Product has been saved."))
            return redirect(reverse("product-web:list"))
        else:
            return redirect("product-web:create", {"form": p_form, "action": "create"})


def product_update_view(request, pk: int):
    if request.method == "GET":
        product = get_object_or_404(Product, pk=pk)
        p_form = ProductForm(instance=product)
        return render(request, "product/update.html", {"form": p_form})
    elif request.method == "POST":
        product = get_object_or_404(Product, pk=pk)
        p_form = ProductForm(data=request.POST, instance=product)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, _("The post has been updated succesfully"))
            return redirect(reverse("product-web:list"))
        else:
            return render(request, "product/update.html", {"form": p_form})
