from django.urls import path
from . import views

app_name = "category"

urlpatterns = [
    path("", views.ProductCategoryListView.as_view(), name="index"),
    path("create", views.ProductCategoryCreateView.as_view(), name="create"),
    path("<pk>/edit", views.ProductCategoryEditView.as_view(), name="edit"),
    path("<pk>/delete", views.ProductCategoryDeleteView.as_view(), name="delete"),
]
