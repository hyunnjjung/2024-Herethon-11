from django import forms
from .models import Profile, Education, Career, Certificate

class EducationModelForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school', 'grade']
        widgets = {
            'school': forms.TextInput(attrs={'placeholder': '학교명&학과명'}),
        }
    def __init__(self, *args, **kwargs):
        super(EducationModelForm, self).__init__(*args, **kwargs)
        # 기존 선택지에서 첫 번째 요소(기본적으로 '--------')를 제거하고, "유형"을 기본 선택으로 추가
        initial_choices = list(self.fields['grade'].choices)[1:]  # 첫 번째 요소를 제외하고 새 목록 생성
        self.fields['grade'].choices = [('', '유형')] + initial_choices

    def clean_grade(self):
        # 폼이 유효성 검사를 통과했을 때, "유형"이라는 값을 공백으로 처리하기 위해 필요
        grade = self.cleaned_data.get('grade')
        if grade == '':
            return None
        return grade
        
class CareerModelForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ['department', 'category']
        widgets = {
            'department': forms.TextInput(attrs={'placeholder': '근무지명&소속 부서'})
        }
    def __init__(self, *args, **kwargs):
        super(CareerModelForm, self).__init__(*args, **kwargs)
        initial_choices = list(self.fields['category'].choices)[1:]
        self.fields['category'].choices = [('', '유형')] + initial_choices

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if category == '':
            return None
        return category
        
class CertificateModelForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['certificate']
        widgets = {
            'certificate': forms.TextInput(attrs={'placeholder': '취득한 자격증을 작성해 주세요.'})
        }
        
class ProfileModelForm(forms.ModelForm):
     class Meta:
        model = Profile
        fields = ['my_image', 'short_intro', 
                  'interest', 'current_job', 'introduce']
        widgets = {
            'my_image': forms.FileInput(attrs={
                'id': 'profile_image',
                'accept': 'image/*',
                'style': 'display: none'  # 입력 필드 숨김
            }),
            'short_intro': forms.TextInput(attrs={'placeholder': '한 줄 소개를 작성해 주세요.'}),
            'interest': forms.TextInput(attrs={'placeholder': '#UI #유통 #IT #생산 #회계 #무역 등'}),
            'current_job': forms.TextInput(attrs={'placeholder': '현재 직무 혹은 희망하는 직무를 작성해 주세요.'}),
            'introduce': forms.TextInput(attrs={'placeholder': '자기소개를 작성해 주세요.'}),
        }