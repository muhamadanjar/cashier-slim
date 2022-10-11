from django.urls import path
from . import views
app_name = "users"
urlpatterns = [
    path("", views.UserListView.as_view(), name="index"),
    path("edit/<pk>", views.UserEditView.as_view(), name="edit"),
    path("delete/<pk>", views.UserDeleteView.as_view(), name="delete"),
]
