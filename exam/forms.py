from django import forms
from .models import Question, TestSet, TestSeries

class QuestionCreationForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('test_set', 'title', 'option1', 'option2', 'option3', 'option4', 'level', 'correct_option')

class TestSetCreationForm(forms.ModelForm):
    model = TestSet
    fields = ('name', 'series', 'level')

class TestSeriesCreationForm(forms.ModelForm):
    model = TestSeries
    fields = ('title', 'exam', 'year')