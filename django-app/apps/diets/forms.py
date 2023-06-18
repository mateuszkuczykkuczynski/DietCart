from django import forms
from django.forms import inlineformset_factory
from .models import Dish, Product, Ingredient


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'brand']


class ProductWidget(forms.Widget):
    template_name = "components/product_search.html"

    def get_context(self, name, value, attrs):
        context = super(ProductWidget, self).get_context(name, value, attrs)
        if value is not None:
            context['widget']['product_name'] = Product.objects.get(id=value).name
            context['widget']['value'] = context['widget']['value'][0]
        return context


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description']

    def save(self, user=None, commit=True):
        obj = super().save(commit=False)
        if user is not None:
            obj.creator = user
        obj.save()
        return obj


ProductFormSet = inlineformset_factory(Dish, Ingredient, can_delete=True, extra=1, fields=['product', 'grammage'],
                                       widgets={'product': ProductWidget()})
