from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import include
from django.urls import path
from users.views import login_view, register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('users.urls')),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('users/', include('users.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
