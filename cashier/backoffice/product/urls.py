from django.urls import path
from . import views
app_name = "product"

urlpatterns =[
    path("", views.ProductListView.as_view(), name='index'),
    path("create", views.ProductCreateView.as_view(), name='create'),
    path("edit/<pk>", views.ProductEditView.as_view(), name='edit'),
    path("delete/<pk>", views.ProductDeleteView.as_view(), name='edit'),
]