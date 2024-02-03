from django.shortcuts import render, redirect
from users.forms import UserProfileForm


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
            print(
                form.errors
            )  
    else:
        form = UserProfileForm()
    return render(request, 'register.html', {'form': form})
