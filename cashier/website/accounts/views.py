from django.contrib.auth import logout, login
from django.shortcuts import redirect, render
from django.views import View
# from cashier.apps.core.utils.core_utils import is_safe_to_redirect
from cashier.website.accounts.forms import CustomAuthenticationForm


class LoginView(View):
    form = CustomAuthenticationForm

    def get(self, request):
        form = self.form(request, data=request.POST or None)
        return render(request, "backoffice/login.html", {"form": form})

    def post(self, request):
        form = self.form(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/backoffice")
        return redirect("accounts:login")


class LogoutView(View):
    def get(self, request):
        logout(request)
        next_url = request.GET.get('next')
        # if next_url and is_safe_to_redirect(url=next_url):
        #     return redirect(next_url)
        return redirect("/")
