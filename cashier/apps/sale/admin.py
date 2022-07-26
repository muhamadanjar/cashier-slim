from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class SaleOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_price', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('id', 'user__username', 'user__email', 'user__first_name', 'user__last_name')
    ordering = ('-created_at',)
    readonly_fields = ('id', 'user', 'status', 'total_price', 'created_at', 'updated_at')
    fieldsets = (
        ('Order', {
            'fields': ('id', 'user', 'status', 'total_price', 'created_at', 'updated_at')
        }),
        ('Items', {
            'fields': ('items',)
        }),
    )
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)