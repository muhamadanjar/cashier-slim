from django import forms

from cashier.apps.product.models import Item, Category


class ProductItemForm(forms.ModelForm):
    class Meta:
        model = Item


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = Category