from django.urls import path
from .views import submit_exam

from .views import ExamView

urlpatterns = [
    #path('', ExamView.as_view(), name='exam'),
    path('', submit_exam, name="submit"),
]
