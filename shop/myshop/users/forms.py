from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
  class Meta(UserCreationForm.Meta):
    model = CustomUser
    fields = UserCreationForm.Meta.fields + ('username', 'first_name', 'last_name', 'email','profile_picture',)

class CustomerUserChangeForm(forms.ModelForm):
  class Meta:
    model = CustomUser
    fields = ('first_name', 'last_name', 'email','profile_picture',)

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'profile_picture']