from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib import messages


def index(request):
    return render(request, 'base.html', {})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            email, password = data['email'], data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                messages.success(request, 'با موفقیت وارد شدید', 'success')
                return redirect('accounts:index')
            return HttpResponse('user not fund')
        return HttpResponse(f'not valid data-- {form.errors}')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})
