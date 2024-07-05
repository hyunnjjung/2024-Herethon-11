from django import forms
from .models import Profile, Education, Career, Certificate

class EducationModelForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school', 'grade']
        # fields = '__all__'
        
class CareerModelForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ['department', 'category']
        
class CertificateModelForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['certificate']
        
class ProfileModelForm(forms.ModelForm):
     class Meta:
        model = Profile
        fields = ['my_image', 'short_intro', 
                  'interest', 'current_job', 'introduce']