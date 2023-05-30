from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


# class RegisterForm(forms.ModelForm):
#     pass_confirmation = forms.PasswordInput()
#
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'first_name', 'last_name', 'password']
#
#     def clean_pass_confirmation(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("pass_confirmation")
#         password2 = self.cleaned_data.get("password")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords do not match")
#         return password2
#
#     def __init__(self, *args, **kwargs):
#         print('a')
#         super(RegisterForm, self).__init__(*args, **kwargs)

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")
