from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateUserForm


def register(request):
    form = CreateUserForm 
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created Successfully')
            return redirect('accounts:login')
            
    context = {'form': form,}
    return render(request, 'accounts/register.html', context)


def log_in(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dest:homepage')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request, 'accounts/login.html')
        
    return render(request, 'accounts/login.html')


def log_out(request):
    logout(request)
    return redirect('dest:homepage')