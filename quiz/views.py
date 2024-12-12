import random
from django.shortcuts import render, redirect
from .models import Question, UserAnswer

def index(request):
    return render(request, 'quiz/index.html')

def start_quiz(request):
    request.session['user_id'] = str(random.randint(1000, 9999))  # Generate a session ID
    return redirect('get_question')

def get_question(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('start_quiz')

    questions_answered = UserAnswer.objects.filter(user_id=user_id).values_list('question_id', flat=True)
    question = Question.objects.exclude(id__in=questions_answered).order_by('?').first()

    if not question:
        return redirect('result')

    return render(request, 'quiz/question.html', {'question': question})

def submit_answer(request, question_id):
    user_id = request.session.get('user_id')
    question = Question.objects.get(id=question_id)
    selected_option = request.POST.get('option')

    is_correct = selected_option == question.correct_option
    UserAnswer.objects.create(
        user_id=user_id,
        question=question,
        selected_option=selected_option,
        is_correct=is_correct
    )

    return redirect('get_question')

def result(request):
    user_id = request.session.get('user_id')
    answers = UserAnswer.objects.filter(user_id=user_id)
    correct_count = answers.filter(is_correct=True).count()
    total_count = answers.count()

    return render(request, 'quiz/result.html', {
        'answers': answers,
        'correct_count': correct_count,
        'total_count': total_count
    })
