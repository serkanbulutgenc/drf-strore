from django.urls import path
from .views import (
    # product_list_create_view,
    # product_retrieve_update_delete_view,
    ProductListCreateView,
    ProductRetrieveUpdateDestroyView,
)

app_name = "product-api"
urlpatterns = [
    # path("products/", product_list_create_view, name="list"),
    path("products/", ProductListCreateView.as_view(), name="list"),
    path("products/<int:pk>/", ProductRetrieveUpdateDestroyView.as_view(), name="retrive"),
    # path("products/<int:pk>/", product_retrieve_update_delete_view, name="retrive"),
]
