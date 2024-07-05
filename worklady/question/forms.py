# forms.py
from django import forms
from .models import Chat_Question, Chat_Answer, Evaluation

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Chat_Question
        fields = ['question_text']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Chat_Answer
        fields = ['answer_text']

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['score']
