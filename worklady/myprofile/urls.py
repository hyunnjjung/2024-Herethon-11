from rest_framework.routers import SimpleRouter
from django.urls import path, include
from . import views
from .views import *

profile_router = SimpleRouter(trailing_slash=False) 
profile_router.register('profile', ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(profile_router.urls)),
    # 검색 테스트
    path('profile/list/', ProfileViewSet.as_view({'get': 'list_view'}), name='profile_list'),
]
