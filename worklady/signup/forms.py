from django import forms
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.http import HttpResponseBadRequest, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

User = CustomUser

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')  
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')  
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user is None:
                raise forms.ValidationError('Invalid email or password.')

        return cleaned_data

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'name', 'birthday', 'phone_number', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class EmailFindForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=64)
    name = forms.CharField(label='Name', max_length=30)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        name = cleaned_data.get('name')

        if email and name:
            if not CustomUser.objects.filter(email=email, name=name).exists():
                raise forms.ValidationError("Email or name does not exist.")
        return cleaned_data