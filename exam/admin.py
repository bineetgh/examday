from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import QuestionCreationForm, TestSetCreationForm, TestSeriesCreationForm
from .models import Question, TestSet, TestSeries

class QuestionAdmin(admin.ModelAdmin):
    add_form = QuestionCreationForm
    form = QuestionCreationForm
    model = Question
    list_display = ['title']

class TestSetAdmin(admin.ModelAdmin):
    add_form = TestSetCreationForm
    form = TestSetCreationForm
    model = TestSet
    list_display = ['name']


class TestSeriesAdmin(admin.ModelAdmin):
    add_form = TestSeriesCreationForm
    form = TestSeriesCreationForm
    model = TestSeries
    list_display = ['title']


admin.site.register(Question, QuestionAdmin)

admin.site.register(TestSet, TestSetAdmin)

admin.site.register(TestSeries, TestSeriesAdmin)