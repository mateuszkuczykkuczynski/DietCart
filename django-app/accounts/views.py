from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy

from .forms import RegisterForm, UserUpdateForm
from django.views import generic

from .models import CustomUser


# class RegisterView(generic.FormView):
#     form_class = RegisterForm
#     template_name = 'accounts/register.html'
#     success_url = reverse_lazy('login')  # TODO Stworzyć monit o poprawnym stworzeniu użytkownika
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
#
#
# class UserUpdateView(generic.UpdateView):
#     form_class = UserUpdateForm
#     template_name = 'accounts/user_update.html'
#     model = CustomUser
