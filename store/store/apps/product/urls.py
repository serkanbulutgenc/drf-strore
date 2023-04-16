from django.urls import path
from .views import (
    product_list_view,
    product_detail_view,
    product_update_view,
    product_create_view,
)

app_name = "product-web"

urlpatterns = [
    path("", product_list_view, name="list"),
    path("create/", product_create_view, name="create"),
    path("<int:pk>/", product_detail_view, name="detail"),
    path("update/<int:pk>/", product_update_view, name="update"),
]
