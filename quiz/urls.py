from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('start/', views.start_quiz, name='start_quiz'),
    path('question/', views.get_question, name='get_question'), 
    path('submit/<int:question_id>/', views.submit_answer, name='submit_answer'), 
    path('question-result/<int:question_id>/', views.question_result, name='question_result'), 
    path('final-result/', views.final_result, name='final_result'), 
]
