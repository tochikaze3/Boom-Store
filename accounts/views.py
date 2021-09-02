
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from  .forms import SignUpForm
from .models import Account

def home_view(request):
    return render(request, "home.html", {})
    
def signup_view(request):
    form = SignUpForm(request.POST)

    if form.is_valid():
        form.save() 
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        store_Name = authenticate(email=email, password=password)
        login(request, store_Name)
        
        return redirect('Account')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})