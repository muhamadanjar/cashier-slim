from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class SaleOrderAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    list_filter = ('status',)
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')
    readonly_fields = ('order_date', 'created_at')
    ordering = ('-created_at',)
    fieldsets = (
        ('Order', {
            'fields': ('user', 'customer', 'name', 'references',
                       'amount_tax', 'amount_price', 'amount_change', 'amount_payment',
                       'status', 'notes'
                       )
        }),
        ('Items', {
            'fields': ('order_lines',)
        }),
    )
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=request.user)


@admin.register(OrderItem)
class AdminOrderItem(admin.ModelAdmin):
    list_display = ("item", 'quantity', 'subtotal',)
