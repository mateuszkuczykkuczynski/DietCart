from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View, generic
from .forms import DishForm, ProductFormSet, ProductForm
from .models import Dish, Product


class DishListView(generic.ListView):
    template_name = 'diets/dish_list.html'
    model = Dish

    def get_queryset(self):
        return Dish.objects.filter(creator=self.request.user)


class DishCreateView(generic.CreateView):
    form_class = DishForm
    template_name = 'diets/dish_create.html'
    success_url = reverse_lazy('dish_list')

    def post(self, request, *args, **kwargs):
        """
        Overriding POST for forwarding current user to form save
        """
        form = self.get_form()
        if form.is_valid():
            form.save(user=request.user)
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)


class DishEditView(generic.TemplateView):
    template_name = 'diets/dish_edit.html'

    def get(self, request, *args, **kwargs):
        dish = get_object_or_404(Dish, pk=kwargs.get('pk'))
        context = self.get_context_data()
        context['form'] = DishForm(instance=dish)
        context['formset'] = ProductFormSet(instance=dish)
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        dish = get_object_or_404(Dish, pk=kwargs.get('pk'))
        form = DishForm(request.POST, instance=dish)
        formset = ProductFormSet(request.POST, instance=dish)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect(reverse_lazy('dish_edit', kwargs={'pk': kwargs.get('pk')}))
        else:
            context = self.get_context_data()
            context['form'] = form
            context['formset'] = formset
            return render(request, template_name=self.template_name, context=context)


class ProductListView(generic.ListView):
    template_name = 'diets/product_list.html'
    model = Product

    def get_queryset(self):
        return Product.objects.all()  # TODO creator field


class ProductCreateView(generic.CreateView):
    template_name = 'diets/product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')


class ProductEditView(generic.UpdateView):
    template_name = 'diets/product_edit.html'
    model = Product
    success_url = reverse_lazy('product_edit')
    form_class = ProductForm
