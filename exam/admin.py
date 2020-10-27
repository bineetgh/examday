from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import QuestionCreationForm
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    add_form = QuestionCreationForm
    form = QuestionCreationForm
    model = Question
    list_display = ['title']

admin.site.register(Question, QuestionAdmin)
