from django.core.paginator import Paginator

from cashier.apps.sale.models import Order
from cashier.backoffice.views import BaseListView, BaseDetailView


class TransactionListView(BaseListView):
    model = Order
    paginator_class = Paginator
    paginate_by = 20
    template_name = "backoffice/sale/index.html"


class TransactionDetailView(BaseDetailView):
    model = Order

