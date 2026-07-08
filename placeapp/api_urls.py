from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'companies', views.CompanyViewSet)
router.register(r'placement-sessions', views.PlacementSessionViewSet)
router.register(r'job-openings', views.JobOpeningViewSet)
router.register(r'job-applications', views.JobApplicationViewSet)
router.register(r'contact-us', views.ContactUsViewSet)
router.register(r'company-register', views.CompanyRegisterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]