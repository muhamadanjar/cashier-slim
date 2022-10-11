from allauth.account.views import PasswordSetView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('backoffice:index')


class MyPasswordSetView(LoginRequiredMixin, PasswordSetView):
    success_url = reverse_lazy('backoffice:index')
