from django.contrib import admin

# Register your models here.
from apps.diets.models import Product, Dish, Ingredient, Meal, Portion, Menu

admin.site.register(Product)
admin.site.register(Dish)
admin.site.register(Ingredient)
admin.site.register(Meal)
admin.site.register(Portion)
admin.site.register(Menu)