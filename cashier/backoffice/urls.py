from django.urls import path, include
from . import views
app_name = "backoffice"
urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path("product/", include("cashier.backoffice.product.urls")),
    path("transactions/", include("cashier.backoffice.transactions.urls")),
    path("users/", include("cashier.backoffice.transactions.urls")),
]
