from django.urls import path
from . import views

urlpatterns = [
    path("", views.WebsiteIndexView.as_view(), name="index")
]
