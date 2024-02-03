from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from users.forms import UserProfileForm


@login_required
def home_view(request):
    return render(request, 'home.html')


def login_view(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = UserProfileForm()
    return render(request, 'register.html', {'form': form})
