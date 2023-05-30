from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy

from .forms import RegisterForm
from django.views.generic import FormView


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
