from django.urls import path
from .views import home_view, login_view, register

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
]
