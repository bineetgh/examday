from django import forms
from .models import Question

class QuestionCreationForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'option1', 'option2', 'option3', 'option4', 'level', 'correct_option')

class TestSetForm(forms.ModelForm):
    model = Question
    fields = ('id', 'correct_option')