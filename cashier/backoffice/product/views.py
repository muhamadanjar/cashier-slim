from cashier.apps.product.forms import ProductItemForm
from cashier.apps.product.models import Item
from cashier.backoffice.views import BaseListView, BaseCreateFormView, BaseFormView, BaseDeleteView, BaseDetailView


class ProductListView(BaseListView):
    model = Item


class ProductCreateView(BaseCreateFormView):
    form_class = ProductItemForm


class ProductEditView(BaseFormView):
    form_class = ProductItemForm


class ProductDeleteView(BaseDeleteView):
    model = Item


class ProductDetailView(BaseDetailView):
    model = Item
