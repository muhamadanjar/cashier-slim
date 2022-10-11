from django import forms

from cashier.apps.product.models import Item, Category


class ProductItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name", "stock", "category", "price", "sell", "description", "image")


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', "slug")
