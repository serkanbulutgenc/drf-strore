from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.core.validators import MinLengthValidator, MaxLengthValidator
from functools import cached_property
from mptt.models import MPTTModel, TreeForeignKey
from mptt.fields import TreeForeignKey as TreeForeignKeyField
from django.utils.text import slugify


# Create your models here.
UNIT = (("kg", "Kilogram"), ("number", "Number"), ("box", "Box"))
TAXES = ((1.0, "%1"), (8.0, "%8"), (18.0, "%18"))


class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=50, help_text=_("Brand Name"))
    slug = models.SlugField(_("Slug"), max_length=50, help_text=_("Brand Slug"))
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True, editable=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["-created_at"]


class Category(MPTTModel):
    name = models.CharField(_("Name"), max_length=50, help_text=_("Category Name"))
    slug = models.SlugField(
        _("Slug"), max_length=50, unique=True, help_text=_("Category Slug")
    )
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True, editable=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    class MPTTMeta:
        order_insertion_by = ["name"]


class ProductActiveManager(models.manager.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Product(models.Model):
    title = models.CharField(
        _("Title"),
        max_length=255,
        help_text=_("Product Title"),
        validators=[MinLengthValidator(3)],
    )
    slug = models.SlugField(
        _("Slug"), max_length=255, unique=True, help_text=_("Product Slug")
    )
    category = TreeForeignKeyField(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        help_text=_("Product Categories"),
        related_name="products",
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True,
        related_name="brand",
        help_text=_("Product Brand"),
    )

    description = models.TextField(
        _("Description"),
        null=True,
        blank=True,
        max_length=1000,
        help_text=_("Product Description"),
        validators=[MaxLengthValidator(1000)],
    )
    # qty = models.IntegerField(_("Quantity"), default=1, help_text=_("Product Quantity"))

    original_price = models.DecimalField(
        _("Original Price"), max_digits=6, decimal_places=2, help_text=_("Product Price")
    )

    sale_price = models.DecimalField(
        _("Sale Price"), max_digits=6, decimal_places=2, help_text=_("Sale Price")
    )

    @cached_property
    def discount_rate(self) -> int:
        return int(100 - ((self.sale_price * 100) / self.original_price))

    is_active = models.BooleanField(
        _("Is Active"), default=True, help_text=_("Is Product Active")
    )
    created_at = models.DateTimeField(
        _("Created Time"), auto_now_add=True, editable=False, help_text=_("Created at")
    )
    updated_at = models.DateTimeField(
        _("Updated Time"), auto_now=True, editable=False, help_text=_("Updated Time")
    )

    objects = models.manager.Manager()
    active = ProductActiveManager()

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("product-web:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.title}"


class Stock(models.Model):
    sku = models.CharField(
        _("SKU"),
        max_length=8,
        unique=True,
        help_text=_("Product SKU"),
        validators=[MinLengthValidator(6)],
    )
    unit = models.CharField(_("Unit"), choices=UNIT, max_length=20, help_text=_("Unit"))
    amount = models.SmallIntegerField(_("Amount"), default=1, help_text=_("Amount"))
    unit_price = models.DecimalField(
        _("Unit Price"), max_digits=5, decimal_places=2, help_text=_("Unit Price")
    )
    tax_rate = models.FloatField(_("Tax Rate"), choices=TAXES, help_text=_("Tax Rate"))
    profit_rate = models.FloatField(_("Profit"), default=20, help_text=_("Profit Rate"))
    product = models.OneToOneField(
        Product,
        verbose_name=_("Product"),
        on_delete=models.CASCADE,
        help_text=_("Product"),
        related_name="stock",
    )
    created_at = models.DateTimeField(
        _("Created At"), auto_now_add=True, editable=False, help_text=_("Created At")
    )
    updated_at = models.DateTimeField(
        _("Updated At"), auto_now=True, editable=False, help_text=_("Updated At")
    )

    def __str__(self):
        return f"{self.sku}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Stock List")
        verbose_name_plural = _("Stock List")
