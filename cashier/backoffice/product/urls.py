from django.urls import path, include
from . import views
app_name = "product"

urlpatterns =[
    path("", views.ProductListView.as_view(), name='index'),
    path("create", views.ProductCreateView.as_view(), name='create'),
    path("<pk>/edit", views.ProductEditView.as_view(), name='edit'),
    path("<pk>/delete", views.ProductDeleteView.as_view(), name='edit'),
    path("category/", include("cashier.backoffice.product.category.urls")),
]
