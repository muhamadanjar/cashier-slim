from cashier.apps.accounts.forms import UserForm
from cashier.apps.accounts.models import User
from cashier.backoffice.views import BaseListView, BaseCreateFormView, BaseFormView, BaseDeleteView


class UserListView(BaseListView):
    model = User
    template_name = "backoffice/users/index.html"


class UserCreateView(BaseCreateFormView):
    form_class = UserForm


class UserEditView(BaseFormView):
    form_class = UserForm


class UserDeleteView(BaseDeleteView):
    model = User
