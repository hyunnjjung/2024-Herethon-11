from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm 
from django.contrib.auth import authenticate, login #추가한 부분

from .models import CustomUser
from rest_framework import serializers
from django.http import JsonResponse
from .tokens import account_activation_token#토큰 생성 함수 추가함
#APIView 상속받기 !
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import AllowAny
#email 본인인증 구현에 필요한 import들
from django.core.mail import send_mail
from django.http import JsonResponse
from django.utils.crypto import get_random_string
from django.http import JsonResponse

from .forms import SignUpForm, LoginForm, EmailFindForm 

User = CustomUser
'''
def save(self, *args, **kwargs):
        if not self.pk:
            self.username = self.email
        super().save(*args, **kwargs)'''

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            #print("valid")
            form.save()
            return redirect('signup_success')
        else:
            #print("notvalid")
            return render(request, 'signup.html', {'form':form})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})

def signup_success(request):
    return render(request, 'signup_success.html')

def join_page(request):
    form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)  
        if form.is_valid():
            username = form.cleaned_data['username']  # 사용자가 입력한 ID(이메일)를 가져옴
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # 로그인 성공
                login(request, user)
                return redirect('home')
            else:
                # 로그인 실패
                print("로그인 실패")
                pass
    else:
        form = LoginForm()  
    return render(request, 'Login.html', {'form': form})

def main_page(request):
    form = LoginForm()
    return render(request, 'Main.html', {'form': form})

def home_page(request):
    return render(request, 'Home.html')

def privacyClause(request):
    return render(request, 'privacyClause.html')

def workladyClause(request):
    return render(request, 'workladyClause.html')

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
            email = form.cleaned_data['id']
            name = form.cleaned_data['name']
            
            masked_email = '***' + email[3:]
            
            message = f"{masked_email} (존재하는 이메일)" if CustomUser.objects.filter(id=email, name=name).exists() else "존재하지 않는 이메일 또는 이름입니다."
            return JsonResponse({'message': message})
        else:
            return JsonResponse(form.errors, status=400)
    else:
        form = EmailFindForm()
    return render(request, 'findEmail.html', {'form': form})

#본인인증 figma형식으로 구현 시도중 ...
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
                'your_email@gmail.com',
                [email],
                fail_silently=False,
            )
            return JsonResponse({'message': '인증 코드가 이메일로 전송되었습니다.'}, status=200)
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