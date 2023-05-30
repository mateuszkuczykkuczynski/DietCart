from django.contrib.auth import views as auth_views
from django.urls import path
from apps.accounts.views import RegisterView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register')
    ]
