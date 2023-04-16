from django.forms import ModelForm
from store.apps.product.models import Product, Category
from mptt.fields import TreeNodeMultipleChoiceField


class ProductForm(ModelForm):
    # categories = TreeNodeMultipleChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = "__all__"
        exclude = ["slug"]
        # help_texts = {"title": "This is title"}

    class Media:
        css = {"all": ["test.css"]}
        js = ["test.js"]
