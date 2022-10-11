from cashier.apps.sale.models import Order
from cashier.backoffice.views import BaseListView


class TransactionListView(BaseListView):
    model = Order
