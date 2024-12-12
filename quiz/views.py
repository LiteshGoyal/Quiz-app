import random
from django.shortcuts import render, redirect
from .models import Question, UserAnswer

def index(request):
    return render(request, 'quiz/index.html')

def start_quiz(request):
    request.session['user_id'] = str(random.randint(1000, 9999))
    request.session['total_correct'] = 0
    request.session['total_attempted'] = 0
    return redirect('get_question')

def get_question(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('start_quiz')

    questions_answered = UserAnswer.objects.filter(user_id=user_id).values_list('question_id', flat=True)
    question = Question.objects.exclude(id__in=questions_answered).order_by('?').first()

    if not question:
        return redirect('final_result')

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

    request.session['total_attempted'] += 1
    if is_correct:
        request.session['total_correct'] += 1

    return redirect('question_result', question_id=question.id)

def question_result(request, question_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('start_quiz')

    answer = UserAnswer.objects.get(user_id=user_id, question_id=question_id)

    return render(request, 'quiz/question_result.html', {
        'answer': answer,
        'total_correct': request.session.get('total_correct', 0),
        'total_attempted': request.session.get('total_attempted', 0)
    })

def final_result(request):
    user_id = request.session.get('user_id')
    answers = UserAnswer.objects.filter(user_id=user_id)
    total_correct = request.session.get('total_correct', 0)
    total_attempted = request.session.get('total_attempted', 0)

    return render(request, 'quiz/final_result.html', {
        'answers': answers,
        'total_correct': total_correct,
        'total_attempted': total_attempted
    })
