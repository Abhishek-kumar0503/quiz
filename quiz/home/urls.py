from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_quiz, name='start_quiz'),
    path('start/', views.start_quiz, name='start_quiz'),
    path('quiz/<int:session_id>/', views.quiz_view, name='quiz_view'),
    path('submit/<int:session_id>/', views.submit_answer, name='submit_answer'),
    path('summary/<int:session_id>/', views.quiz_summary, name='quiz_summary'),
]
