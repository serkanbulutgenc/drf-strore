from django.urls import path
from store.apps.dashboard.views import DashboardIndex

app_name = "dashboard"
urlpatterns = [path("", DashboardIndex.as_view(), name="index")]
