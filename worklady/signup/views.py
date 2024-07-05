from django.shortcuts import get_object_or_404, render, redirect

from question.models import Answer, Question, Rating, Tag
from .forms import SignUpForm, LoginForm, EmailFindForm
from django.contrib.auth import authenticate, login
from .models import CustomUser
from django.http import HttpResponseRedirect, JsonResponse
from .tokens import account_activation_token
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import SetPasswordForm
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status, serializers
from django.urls import reverse
from django.db.models import Q
from django.db.models import Avg

User = CustomUser

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup_success')  # 회원가입 성공 후 signup_success 페이지로 리다이렉트
        else:
            # 폼이 유효하지 않은 경우, 에러와 함께 다시 signup 페이지를 렌더링합니다.
            return render(request, 'signup1.html', {'form': form})
    else:
        form = SignUpForm()
    
    return render(request, 'signup1.html', {'form': form})
def signup_success(request):
    return render(request, 'signup4.html')

def join_page(request):
    form = SignUpForm()
    return render(request, 'signup1.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') 
            else:
                form.add_error(None, '유효하지 않은 이메일 또는 비밀번호입니다.')
    else:
        form = LoginForm()
    
    return render(request, 'login1.html', {'form': form})

def main_page(request):
    form = LoginForm()
    return render(request, 'Main.html', {'form': form})

def home_page(request):
    return render(request, 'Home.html')

def signup2_view(request):
    return render(request, 'signup2.html')

def signup3_view(request):
    return render(request, 'signup3.html')

def findemail(request):
    return render(request, 'findEmail.html')

#이메일 찾기 구현 == 완료 ;)
class EmailFindSerializer(serializers.Serializer):
    id = serializers.EmailField(max_length=64, required=True)

    def validate_id(self, value):
        if not CustomUser.objects.filter(id=value).exists():
            raise serializers.ValidationError("존재하지 않는 이메일입니다.")
        return value

def findemail(request):
    if request.method == 'POST':
        form = EmailFindForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            
            masked_email = '***' + email[3:]
            
            message = f"{masked_email} (존재하는 이메일)" if CustomUser.objects.filter(email=email, name=name).exists() else "존재하지 않는 이메일 또는 이름입니다."
            return JsonResponse({'message': message})
        
        else:
            return JsonResponse(form.errors, status=400)
   
    else:
        form = EmailFindForm()
    return render(request, 'findEmail.html', {'form': form})

#본인인증 figma형식으로 구현 완료;)
# 이메일 인증 코드 전송 뷰
def send_verification_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            verification_code = get_random_string(length=6, allowed_chars='0123456789')
            request.session['verification_code'] = verification_code

            send_mail(
                '[워크레디] 이메일 인증 코드',
                f'워크레디를 찾아주셔서 감사합니다. 인증 코드는 {verification_code}입니다.',
                'your_email@gmail.com',  # 발신자 이메일 설정
                [email],
                fail_silently=False,
            )
            return JsonResponse({'message': '인증 코드가 이메일로 전송되었습니다.'}, status=200)
        else:
            return JsonResponse({'error': '이메일 주소를 입력해주세요.'}, status=400)
    else:
        return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)

# 이메일 인증 코드 검증 뷰
def verify_code(request):
    if request.method == 'POST':
        input_code = request.POST.get('verification_code')

        if input_code and input_code == request.session.get('verification_code'):
            return JsonResponse({'message': '인증 성공'}, status=200)

        return JsonResponse({'error': '인증 코드가 잘못되었습니다.'}, status=400)

    return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)

# 유저 활성화 뷰
class UserActivateView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, uid, token):
        try:
            real_uid = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=real_uid)
            if user is not None:
                payload = jwt_decode_handler(token)
                user_id = jwt_payload_get_user_id_handler(payload)
                if int(real_uid) == int(user_id):
                    user.is_active = True
                    user.save()
                    return Response(user.email + '계정이 활성화 되었습니다', status=status.HTTP_200_OK)
                    
                return Response('인증에 실패하였습니다', status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response('인증에 실패하였습니다', status=status.HTTP_400_BAD_REQUEST)

        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
            return Response('인증에 실패하였습니다', status=status.HTTP_400_BAD_REQUEST)

#비밀번호 재설정 구현 완료 ;) 
#이메일로 비밀번호 재설정 링크 전송
def send_reset_password_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            user = User.objects.filter(email=email).first()
            if user:
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))

                email_subject = '[워크레디] 비밀번호 재설정 링크'
                email_message = f'비밀번호를 재설정하려면 다음 링크를 클릭하세요: \n\n' \
                                f'{request.build_absolute_uri(reverse("reset_password", kwargs={"uidb64": uid, "token": token}))}'

                send_mail(
                    email_subject,
                    email_message,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                return JsonResponse({'message': '이메일로 비밀번호 재설정 링크를 보냈습니다.'}, status=200)
            else:
                return JsonResponse({'error': '입력한 이메일로 등록된 사용자가 없습니다.'}, status=400)
        else:
            return JsonResponse({'error': '이메일을 입력해주세요.'}, status=400)

    return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)

def verify_reset_password_token(uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        if user and default_token_generator.check_token(user, token):
            return user
        else:
            return None
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return None

def reset_password(request, uidb64, token):
    user = verify_reset_password_token(uidb64, token)
    if user:
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'password_reset_complete.html')
        else:
            form = SetPasswordForm(user)
        return render(request, 'reset_password.html', {'form': form})
    else:
        return render(request, 'password_reset_invalid.html')


def find_pw_page(request):
    return render(request, 'findPw.html')

def password_reset_complete(request):
    return render(request, 'password_reset_complete.html')

#소셜로그인 성공 후 돌아갈 페이지
def socialSuccess(request):
    return render(request, 'main copy.html')


def questionlist(request):
    query = request.GET.get('q', '')
    questions = Question.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))

    filter_option = request.GET.get('filter', '')
    if filter_option == 'answered':
        questions = questions.filter(answers__isnull=False).distinct()
    elif filter_option == 'unanswered':
        questions = questions.filter(answers__isnull=True)

    questions = questions.order_by('-created_at')

    return render(request, 'genqna1.html', {'questions': questions})


def askquestion(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        tags_input = request.POST.get('tags')

        # Check if title and content are not empty
        if not title or not content:
            return render(request, 'genqna5.html', {'error': 'Title and Content cannot be empty.'})

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
        return redirect('questionlist')  # Adjust this according to your URL configuration

    return render(request, 'genqna5.html')


def qtag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    questions = tag.question_set.all()
    return render(request, 'genqna1tag.html', {'tag': tag, 'questions': questions})



def questiondetail(request, pk):
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
    
    return render(request, 'genqna2.html', context)