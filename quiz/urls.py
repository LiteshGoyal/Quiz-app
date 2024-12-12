from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Landing page
    path('start/', views.start_quiz, name='start_quiz'),  # Start the quiz
    path('question/', views.get_question, name='get_question'),  # Fetch a random question
    path('submit/<int:question_id>/', views.submit_answer, name='submit_answer'),  # Submit an answer
    path('question-result/<int:question_id>/', views.question_result, name='question_result'),  # Show result for the last question
    path('final-result/', views.final_result, name='final_result'),  # Final result when no more questions
]
