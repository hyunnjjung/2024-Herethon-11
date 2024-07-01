from rest_framework.routers import SimpleRouter
from django.urls import path, include
# from .views import ProfileViewSet, EducationViewSet, CareerViewSet, CertificateViewSet
from .views import ProfileViewSet

profile_router = SimpleRouter(trailing_slash=False) 
profile_router.register('profile', ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(profile_router.urls)),
]
