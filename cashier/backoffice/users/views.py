from django.views.generic.edit import BaseCreateView

from cashier.apps.accounts.forms import UserForm
from cashier.apps.accounts.models import User
from cashier.backoffice.views import BaseListView, BaseCreateFormView


class UserListView(BaseListView):
    model = User
    template_name = "backoffice/users/index.html"


class UserCreateView(BaseCreateView):
    form_class = UserForm
