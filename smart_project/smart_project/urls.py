from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path
from users.views import login_view, register, home_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
