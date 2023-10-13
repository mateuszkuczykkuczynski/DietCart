from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='Name')
    brand = models.CharField(max_length=256, verbose_name='Brand')
    creator = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, null=True, blank=True, verbose_name="User")

    def __str__(self):
        return f"{self.name} {self.brand}"


class Dish(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=1024, verbose_name='Description', blank=True, null=True)
    creator = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, verbose_name="User")

    def __str__(self):
        return f"{self.name}"


class Ingredient(models.Model):
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, verbose_name="Product"
    )
    dish = models.ForeignKey(
        'Dish', on_delete=models.CASCADE, verbose_name="Dish"
    )
    grammage = models.IntegerField(verbose_name="Grammage")

    def __str__(self):
        return f"{self.product} {self.grammage}g"


class Meal(models.Model):
    name = models.CharField(max_length=256, verbose_name='Meal')
    dishes = models.ManyToManyField('Dish')


class Portion(models.Model):
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, verbose_name="Product"
    )
    meal = models.ForeignKey(
        'Meal', on_delete=models.CASCADE, verbose_name="Meal"
    )
    grammage = models.IntegerField(verbose_name="Grammage")


class Menu(models.Model):
    name = models.CharField(max_length=256, verbose_name="Name")
    meals = models.ManyToManyField('Meal', verbose_name="Meals")
