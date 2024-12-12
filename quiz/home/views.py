from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, QuizSession, Answer
import random

# new quiz session
def start_quiz(request):
    session = QuizSession.objects.create()
    return redirect('quiz_view', session_id=session.id)

def quiz_view(request, session_id):
    session = get_object_or_404(QuizSession, id=session_id)
    
    # Fetch all unanswered questions for this session
    answered_questions = Answer.objects.filter(session=session).values_list('question_id', flat=True)
    remaining_questions = Question.objects.exclude(id__in=answered_questions)

    if not remaining_questions.exists():
        return redirect('quiz_summary', session_id=session.id)

    question = random.choice(list(remaining_questions))

    context = {
        'session': session,
        'question': question,
    }
    return render(request, 'quiz.html', context)

# Submit answer for a question
def submit_answer(request, session_id):
    session = get_object_or_404(QuizSession, id=session_id)
    question_id = request.POST.get('question_id')
    selected_option = request.POST.get('selected_option')

    question = get_object_or_404(Question, id=question_id)
    is_correct = (selected_option == question.correct_option)

    Answer.objects.create(session=session, question=question, selected_option=selected_option, is_correct=is_correct)

    return redirect('quiz_view', session_id=session.id)

# Show quiz summary after completion
def quiz_summary(request, session_id):
    session = get_object_or_404(QuizSession, id=session_id)
    answers = Answer.objects.filter(session=session)

    correct_count = answers.filter(is_correct=True).count()
    incorrect_count = answers.filter(is_correct=False).count()

    context = {
        'session': session,
        'answers': answers,
        'correct_count': correct_count,
        'incorrect_count': incorrect_count,
    }
    return render(request, 'summary.html', context)
