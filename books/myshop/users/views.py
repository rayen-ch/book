from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomerUserChangeForm
from django.contrib.auth.decorators import login_required

def register(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST, request.FILES)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
  
  else:
    form = CustomUserCreationForm()
  
  return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):
  return render(request, 'users/profile.html')

@login_required
def edit_profile(request):
  if request.method == 'POST':
    form = CustomerUserChangeForm(request.POST, request.FILES, instance=request.user)
    if form.is_valid():
      form.save()
      return redirect('profile')
  else: 
    form = CustomerUserChangeForm(instance=request.user)
  
  return render(request, 'users/edit_profile.html',{'form':form})