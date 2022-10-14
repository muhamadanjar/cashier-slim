from django.core.paginator import Paginator

from cashier.apps.product.forms import ProductCategoryForm
from cashier.apps.product.models import Category
from cashier.backoffice.views import BaseListView, BaseDeleteView, BaseCreateFormView, BaseFormView


class ProductCategoryListView(BaseListView):
    model = Category
    paginator_class = Paginator
    paginate_by = 20
    template_name = "backoffice/product/category_list.html"


class ProductCategoryCreateView(BaseCreateFormView):
    form_class = ProductCategoryForm
    template_name = "backoffice/product/form.html"


class ProductCategoryEditView(BaseFormView):
    form_class = ProductCategoryForm
    model = Category
    template_name = "backoffice/product/form.html"


class ProductCategoryDeleteView(BaseDeleteView):
    model = Category

