from django.shortcuts import render
from users.forms import UserProfileForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        is_authenticated = request.user.is_authenticated
        return render(
            request, 'users/home.html', {'is_authenticated': is_authenticated}
        )


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


class SignUp(CreateView):
    form_class = UserProfileForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('home')
