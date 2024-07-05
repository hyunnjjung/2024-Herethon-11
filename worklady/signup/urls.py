from django.urls import path, include
from .views import signup, signup_success, join_page, login_page, main_page, home_page, findemail,send_verification_email, verify_code, reset_password,password_reset_complete
from .views import UserActivateView
from django.contrib import admin
from . import views

urlpatterns = [
    path('signup/', signup, name = 'signup'),
    path('signup/success', signup_success, name = 'signup_success'),
    path('join/',join_page, name='join'),
    path('login/',login_page, name='login'),
    path('main/', main_page, name='main'),
    path('home/', home_page, name='home'),
    path('signup2/', views.signup2_view, name='signup2'),
    path('signup3/', views.signup3_view, name='signup3'),
    path('findemail/', findemail, name='findemail'),
    path('activate/<str:uid>/<str:token>/', UserActivateView.as_view(), name='activate'),
    path('send_verification_email/', send_verification_email, name='send_verification_email'),
    path('verify_code/', verify_code, name='verify_code'),
    path('reset_password/<str:uidb64>/<str:token>/', reset_password, name='reset_password'),
    path('find_pw/', views.find_pw_page, name='find_pw'),
    path('send_reset_password_email/', views.send_reset_password_email, name='send_reset_password_email'),
    path('password_reset_complete/',password_reset_complete, name='password_reset_complete'),
    path('rest-auth/', include('dj_rest_auth.urls')),
    #소셜로그인 성공 후 기본 url path 화면으로 넘어가게 설정 -> 추후 / path 사용시 메인페이지로 view바꾸기 가능
    path('', views.socialSuccess, name="socialSuccess"),
    
]