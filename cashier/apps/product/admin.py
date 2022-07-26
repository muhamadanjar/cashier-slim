from django.contrib import admin
from .models import Item, Category, Attribute, AttributeValue


@admin.register(Item)
class ProductItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'stock', 'category', 'description',
                    'price', 'sell', 'image', 'user_id',
                    'created_at', 'updated_at')


@admin.register(Category)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')


@admin.register(Attribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_order', 'created_at', 'updated_at', 'attribute_values')
