from django import forms

from cashier.apps.accounts.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
