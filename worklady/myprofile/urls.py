from django.urls import path , include
from . import views
from .views import *

urlpatterns = [
    path('profile/list/', profile_list, name='profile_list'),
    path('create_profile1', views.create_profile1, name='create_profile1'),
    path('user_detail/', views.user_detail, name='user_detail'),
    path('profile_detail/<int:profile_id>/', views.profile_detail, name="profile_detail"),
    path('profile_update/<int:profile_id>/', views.profile_update, name="profile_update"),
]


