from django.urls import path
from django.views.generic import TemplateView

# from .views import
from cashier.apps.accounts.views import MyPasswordChangeView
from cashier.website.accounts.views import LogoutView, LoginView

app_name = "accounts"

urlpatterns = [
    path("change-password", MyPasswordChangeView.as_view(), name="change_password"),
    path("set-password", MyPasswordChangeView.as_view(), name="set_password"),
    path("reset-password", MyPasswordChangeView.as_view(), name="reset_password"),
    path('auth-logout/', TemplateView.as_view(template_name="account/logout-success.html"), name='pages-logout'),
    path('auth-lockscreen/', TemplateView.as_view(template_name="account/lock-screen.html"), name='pages-lockscreen'),
    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("register", LogoutView.as_view(), name="register"),
]
