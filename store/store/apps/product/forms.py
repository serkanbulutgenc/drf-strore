from django.forms import ModelForm
from store.apps.product.models import Product, Category
from mptt.fields import TreeNodeMultipleChoiceField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Submit,
    Layout,
    Fieldset,
    Field,
    Div,
    Button,
    HTML,
    ButtonHolder,
)
from crispy_bootstrap5.bootstrap5 import FloatingField


class ProductForm(ModelForm):
    # categories = TreeNodeMultipleChoiceField(queryset=Category.objects.all())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            FloatingField("title"),
            FloatingField("brand", "category"),
            Field("description", css_class="cls1 cls2"),
            "original_price",
            "sale_price",
            # HTML("<span>This is html</span>"),
            "is_active",
            ButtonHolder(Submit("save", "Save changes"), Button("cancel", "Cancel")),
        )
        self.helper.form_id = "form-id"
        self.helper.form_class = "form-class"
        self.helper.form_method = "POST"
        self.helper.form_show_labels = False

    class Meta:
        model = Product
        fields = "__all__"
        exclude = ["slug"]
        # help_texts = {"title": "This is title"}

    class Media:
        css = {"all": ["test.css"]}
        js = ["test.js"]
