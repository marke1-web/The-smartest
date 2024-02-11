from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required


@csrf_protect
@login_required(login_url='login')
def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'users/profile.html')


@csrf_protect
def home_view(request):
    return render(request, 'users/home.html')  # Render the main page


@csrf_protect
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(
                request, user
            )  # Automatically log in the user after registration
            return redirect('home')  # Redirect to the main page
        return render(request, 'users/register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@csrf_protect
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the main page after login
        else:
            return render(
                request,
                'users/login.html',
                {'error': 'Неверное имя пользователя или пароль.'},
            )
    return render(request, 'users/login.html')


@csrf_protect
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')  # Redirect to the main page after logout
