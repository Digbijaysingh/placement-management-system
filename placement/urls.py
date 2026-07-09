from django.contrib import admin
from django.urls import path, include
from placeapp import views as placeapp_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Placement Management API",
        default_version='v1',
        description="API documentation for Placement Management System",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', placeapp_views.homepage, name='home'),
    path('', include('placeapp.urls')),
    path('api/', include('placeapp.api_urls')),   # <-- ADD THIS LINE
    path(
    'swagger/',
    schema_view.with_ui('swagger', cache_timeout=0),
    name='schema-swagger-ui'
),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)