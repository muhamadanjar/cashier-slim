from django.core.paginator import Paginator

from cashier.apps.product.forms import ProductItemForm
from cashier.apps.product.models import Item
from cashier.backoffice.views import BaseListView, BaseCreateFormView, BaseFormView, BaseDeleteView, BaseDetailView


class ProductListView(BaseListView):
    model = Item
    paginator_class = Paginator
    paginate_by = 10
    template_name = "backoffice/product/index.html"


class ProductCreateView(BaseCreateFormView):
    template_name = "backoffice/product/form.html"
    form_class = ProductItemForm

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(user=self.request.user, **self.get_form_kwargs())


class ProductEditView(BaseFormView):
    form_class = ProductItemForm
    model = Item
    template_name = "backoffice/product/form.html"

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(instance=self.get_object(), user=self.request.user, **self.get_form_kwargs())


class ProductDeleteView(BaseDeleteView):
    model = Item


class ProductDetailView(BaseDetailView):
    model = Item
