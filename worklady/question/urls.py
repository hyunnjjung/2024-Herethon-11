from django.urls import path, re_path
from . import views
from .views import *

urlpatterns = [
    path('question/ask/', views.ask_question, name='ask_question'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('question/', views.question_list, name='question_list'),
    path('question/<int:pk>/answer_create', views.answer_create, name='answer_create'),
    re_path(r'^question/tag/(?P<slug>[-\w]+)/$', views.tag, name='tag'),
    path('my-questions/', views.my_questions, name='my_questions'),
    path('mentor/<int:mentor_id>/chat/', views.chat_view, name='chat_view'),
    path('<int:mentor_id>/my_answers/', my_answers_view, name='my_answers_view'),
]
