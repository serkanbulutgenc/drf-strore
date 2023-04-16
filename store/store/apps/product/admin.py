from django.contrib.admin import register, ModelAdmin
from mptt.admin import DraggableMPTTAdmin
from .models import Product, Category

# Register your models here.


@register(Category)
class CategoryMPTTAdmin(DraggableMPTTAdmin):
    list_display = ["tree_actions", "indented_title", "name", "slug"]
    list_display_links = ["indented_title"]


@register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ["title", "sale_price", "qty", "is_active"]
    search_fields = ["title"]
    list_filter = ["created_at", "is_active"]
    prepopulated_fields = {"slug": ["title"]}
