from django.contrib import admin
from .models import Question, UserAnswer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'correct_option')
    list_filter = ('correct_option',)
    search_fields = ('question_text',)
    ordering = ('id',)

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'question', 'selected_option', 'is_correct', 'answered_at')
    list_filter = ('is_correct', 'answered_at')
    search_fields = ('user_id', 'question__question_text')
    ordering = ('-answered_at',)
