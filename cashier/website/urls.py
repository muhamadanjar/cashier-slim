from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.WebsiteIndexView.as_view(), name="index"),
    path("accounts", include("cashier.website.accounts.urls"), name="accounts"),
]
