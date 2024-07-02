from django.urls import path, include
from .views import signup, signup_success, join_page, login_page, main_page, home_page,privacyClause,workladyClause, findemail,send_verification_email, verify_code
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
    path('privacyClause/', privacyClause, name='privacyClause'),
    path('workladyClause/', workladyClause, name='workladyClause'),
    path('findemail/', findemail, name='findemail'),
    path('activate/<str:uid>/<str:token>/', UserActivateView.as_view(), name='activate'),
    path('send_verification_email/', send_verification_email, name='send_verification_email'),
    path('verify_code/', verify_code, name='verify_code'),
    #path('find_pw/',views.PwResetEmailSendView.as_view()),
    #path('pwchange/<str:uid>/<str:token>',views.PasswordChangeView.as_view(), name ='pwchange'),
    #path('pwchange/<str:uid>/<str:token>/', views.PasswordChangeView.as_view(), name='pwchange'),
    path('rest-auth/', include('dj_rest_auth.urls')),
]