from django.urls import path, include
from .views import DishListView, DishCreateView, DishEditView, ProductCreateView, ProductEditView, ProductListView

urlpatterns = [
    path('dish/', DishListView.as_view(), name='dish_list'),
    path('dish/create/', DishCreateView.as_view(), name='dish_create'),
    path('dish/<int:pk>/edit/', DishEditView.as_view(), name='dish_edit'),
    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', ProductEditView.as_view(), name='product_edit'),
    path('api/', include('apps.diets.diets_api.urls'))
]
