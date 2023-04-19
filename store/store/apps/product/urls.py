from django.urls import path
from .views import (
    ProductCreate,
    ProductList,
    ProductUpdate,
    ProductDetail,
)

app_name = "product-web"

urlpatterns = [
    path("", ProductList.as_view(), name="list"),
    path("create/", ProductCreate.as_view(), name="create"),
    path("<int:pk>/", ProductDetail.as_view(), name="detail"),
    path("update/<int:pk>/", ProductUpdate.as_view(), name="update"),
]
