from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, SignUp

urlpatterns = [
    path(
        'signup/',
        SignUp.as_view(template_name='users/signup.html'),
        name='signup',
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout',
    ),
    path(
        'login/',
        CustomLoginView.as_view(template_name='users/login.html'),
        name='login',
    ),
]
