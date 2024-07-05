from django.urls import path , include
from . import views
from .views import *

urlpatterns = [
    path('profile/list/', profile_list, name='profile_list'),
    path('profile/interest/<str:interest>/', keyword_list1, name='keyword_list1'),
    path('profile/interest/<str:interest1>/<str:interest2>/', keyword_list2, name='keyword_list2'),
    path('create_profile1', views.create_profile1, name='create_profile1'),
    path('user_detail/', views.user_detail, name='user_detail'),
    path('profile_detail/<int:profile_id>/', views.profile_detail, name="profile_detail"),
    path('profile_update/<int:profile_id>/', views.profile_update, name="profile_update"),
    path('main/', views.main, name="main"),
]


