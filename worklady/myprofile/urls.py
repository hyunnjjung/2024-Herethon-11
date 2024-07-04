from rest_framework.routers import SimpleRouter
from django.urls import path, include
from . import views
from .views import *

profile_router = SimpleRouter(trailing_slash=False) 
profile_router.register('profile', ProfileViewSet, basename='profile')

education_router = SimpleRouter(trailing_slash=False)
education_router.register('education', EducationViewSet, basename='education')

career_router = SimpleRouter(trailing_slash=False)
career_router.register('career', CareerViewSet, basename='career')

certificate_router = SimpleRouter(trailing_slash=False)
certificate_router.register('certificate', CertificateViewSet, basename='certificate')

urlpatterns = [
    path('', include(profile_router.urls)),
    # 검색 테스트
    path('profiles/list/', ProfileViewSet.as_view({'get': 'list_view'}), name='profile_list'),
    path('profile/<int:profile_id>/', include(education_router.urls)),
    path('profile/<int:profile_id>/', include(career_router.urls)),
    path('profile/<int:profile_id>/', include(certificate_router.urls)),
]
