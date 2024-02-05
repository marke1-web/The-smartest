from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView
from users.views import HomeView, CustomLoginView, ProfileView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    # Маршруты для аутентификации
    path('login/', CustomLoginView.as_view(), name='login'),
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout',
    ),
    path('register/', RedirectView.as_view(url='/auth/signup/')),
    path(
        'profile/',
        login_required(
            ProfileView.as_view(template_name='users/profile.html')
        ),
        name='profile',
    ),
    # include ваших собственных маршрутов
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
