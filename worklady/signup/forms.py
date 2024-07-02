from django import forms
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.http import HttpResponseBadRequest, JsonResponse
from .models import CustomUser

User = CustomUser

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError('Invalid username or password.')

        return cleaned_data

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('id', 'name', 'birthday', 'password', 'password_confirm', 'phone_number')
        widgets = {
            'password': forms.PasswordInput(),
            'password_confirm': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # 로그인 성공
                login(request, user)
                return redirect('home')
            else:
                # 로그인 실패
                print("로그인 실패")
    else:
        form = LoginForm()
    return render(request, 'Login.html', {'form': form})

class EmailFindForm(forms.Form):
    id = forms.EmailField(label='이메일', max_length=64)
    name = forms.CharField(label='이름', max_length=30)

    def clean(self):
        cleaned_data = super().clean()
        id = cleaned_data.get('id')
        name = cleaned_data.get('name')

        if id and name:
            if not CustomUser.objects.filter(id=id, name=name).exists():
                raise forms.ValidationError("존재하지 않는 이메일 또는 이름입니다.")
        return cleaned_data