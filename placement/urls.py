from django.contrib import admin
from django.urls import path, include
from placeapp import views as placeapp_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', placeapp_views.homepage, name='home'),
    path('', include('placeapp.urls')),
    path('api/', include('placeapp.api_urls')),   # <-- ADD THIS LINE
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)