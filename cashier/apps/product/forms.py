from django import forms

from cashier.apps.product.models import Item, Category


class ProductItemForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ProductItemForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(ProductItemForm, self).save(commit=False)
        instance.user = self.user
        instance.save()
        return instance

    class Meta:
        model = Item
        fields = ("name", "stock", "category", "price", "sell", "description", "image")


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', "slug")
