from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, View):

    def get(self, request):
        context = {}
        context['heading'] = "Dashboard"
        context['pageview'] = "Dashboards"
        return render(request, 'backoffice/dashboard.html', context)


class PagesLoginView(View):
    def get(self, request):
        return render(request, 'backoffice/login.html')