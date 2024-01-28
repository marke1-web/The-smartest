from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += [
    path('users/', include('users.urls')),
]
urlpatterns += [
    path('', RedirectView.as_view(url='/users/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
