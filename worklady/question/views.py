from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from coin.models import Coin

from .forms import QuestionForm, AnswerForm, EvaluationForm
from .models import MentorProfile, Question, Answer, Rating
from django.db.models import Q
from .models import Tag
from django.db.models import Avg
from django.http import HttpResponseRedirect

@login_required
def chat_view(request, mentor_id):
    mentor = get_object_or_404(MentorProfile, id=mentor_id)
    questions = Question.objects.filter(mentor).order_by('created_at')

    if request.method == 'POST':
        if request.user == mentor.user:
            # Mentor answering the most recent unanswered question
            if 'answer_question' in request.POST:
                question = questions.filter(is_answered=False).first()
                if question:
                    a_form = AnswerForm(request.POST)
                    if a_form.is_valid():
                        answer = a_form.save(commit=False)
                        answer.question = question
                        answer.save()
                        question.is_answered = True
                        question.save()
                        return redirect('chat_view', mentor_id=mentor_id)

            # Accepting or rejecting a question
            elif 'accept_question' in request.POST:
                question_id = request.POST.get('question_id')
                question = get_object_or_404(Question, id=question_id)
                question.is_accepted = True
                question.save()
                return redirect('chat_view', mentor_id=mentor_id)

            elif 'reject_question' in request.POST:
                question_id = request.POST.get('question_id')
                question = get_object_or_404(Question, id=question_id)
                question.is_accepted = False
                question.save()
                return redirect('chat_view', mentor_id=mentor_id)

        else:
            # User asking a question
            if 'ask_question' in request.POST:
                q_form = QuestionForm(request.POST)
                if q_form.is_valid():
                    question = q_form.save(commit=False)
                    question.asker = request.user
                    question.mentor = mentor
                    question.is_accepted = True  # Automatically accept the question
                    question.save()
                    return redirect('chat_view', mentor_id=mentor_id)

            # Handling evaluation
            elif 'evaluate_answer' in request.POST:
                answer_id = request.POST.get('answer_id')
                answer = get_object_or_404(Answer, id=answer_id)
                e_form = EvaluationForm(request.POST)
                if e_form.is_valid():
                    evaluation = e_form.save(commit=False)
                    evaluation.answer = answer
                    evaluation.save()
                    return redirect('chat_view', mentor_id=mentor_id)

    else:
        q_form = QuestionForm()
        a_form = AnswerForm()
        e_form = EvaluationForm()


    context = {
        'mentor': mentor,
        'questions': questions,
        'q_form': q_form,
        'a_form': a_form,
        'e_form': e_form,
    }
    return render(request, 'mentorship/chat.html', context)



@login_required
def my_questions(request):
    
    questions = Question.objects.filter(author=request.user).order_by('-created_at')

    filter_option = request.GET.get('filter', '')
    if filter_option == 'answered':
        questions = questions.filter(answers__isnull=False).distinct()
    elif filter_option == 'unanswered':
        questions = questions.filter(answers__isnull=True)
        
    return render(request, 'question/my_questions.html', {'questions': questions})


def question_list(request):
    query = request.GET.get('q', '')
    questions = Question.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))

    filter_option = request.GET.get('filter', '')
    if filter_option == 'answered':
        questions = questions.filter(answers__isnull=False).distinct()
    elif filter_option == 'unanswered':
        questions = questions.filter(answers__isnull=True)

    questions = questions.order_by('-created_at')

    return render(request, 'question/question_list.html', {'questions': questions})

def tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    questions = tag.question_set.all()
    return render(request, 'question/tag.html', {'tag': tag, 'questions': questions})


@login_required
def ask_question(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        tags_input = request.POST.get('tags')

        # Check if title and content are not empty
        if not title or not content:
            return render(request, 'question/ask_question.html', {'error': 'Title and Content cannot be empty.'})

        # Create a new question associated with the current user
        new_question = Question(
            title=title,
            content=content,
            author=request.user, # Associate the question with the logged-in user
        )
        
        new_question.save()

        # Process tags and associate them with the question
        if tags_input:
            tags_list = tags_input.split('#')
            for tag_text in tags_list:
                tag_text = tag_text.strip()
                if tag_text:
                    tag_obj, created = Tag.objects.get_or_create(name=tag_text)
                    new_question.tags.add(tag_obj)

        # Redirect to a success page or another view
        return redirect('question_list')  # Adjust this according to your URL configuration

    return render(request, 'question/ask_question.html')


@login_required
def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    
    # Check if current user has answered this question
    user_has_answered = question.answers.filter(author=request.user).exists()
    
    # Handle rating submission
    if request.method == 'POST' and 'answer_id' in request.POST and 'rating' in request.POST:
        answer_id = request.POST.get('answer_id')
        rating_value = int(request.POST.get('rating'))
        
        try:
            answer = Answer.objects.get(id=answer_id, question=question)
            if answer.author != request.user:  # Prevent authors from rating their own answers
                # Check if the user has already rated this answer
                existing_rating = Rating.objects.filter(answer=answer, user=request.user).first()
                if existing_rating:
                    existing_rating.value = rating_value
                    existing_rating.save()
                else:
                    new_rating = Rating(answer=answer, user=request.user, value=rating_value)
                    new_rating.save()
        except Answer.DoesNotExist:
            return HttpResponseRedirect(request.path)  # Answer not found
    
    # Retrieve answers with average rating
    answers = question.answers.annotate(avg_rating=Avg('ratings__value'))
    
    context = {
        'question': question,
        'user_has_answered': user_has_answered,
        'answers': answers,
    }
    
    return render(request, 'question/question_detail.html', context)

@login_required
def answer_create(request, pk):
    question = get_object_or_404(Question, pk=pk)
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            answer = Answer.objects.create(
                question=question,
                content=content,
                author=request.user,
            )
            return redirect('question_detail', pk=question.pk)  # Redirect to the question detail page
    
    # If request method is not POST or content is empty, render the template with the question
    return render(request, 'question/answer_create.html', {'question': question})


