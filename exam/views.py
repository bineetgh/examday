from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import TemplateView
from exam.models import Question
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin


class ExamView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    raise_exception = True
    template_name = 'pages/exam.html'

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['questions'] = Question.objects.all()[:5]
    return context

def submit_exam(request):
    score = 0
    total = 0
    ans = {}
    qs = []
    if request.method == 'POST':
        ans = request.POST
        ids = []
        
        for key in ans.keys():
            if key.isnumeric():
                ids.append(key)
        qs = Question.objects.filter(pk__in=ids)
        for q in qs:
            total = total + 1
            if q.correct_option == int(ans.get(str(q.id))):
                score = score + 1

        # If this is a GET (or any other method) create the default form.
    else:
        qs = Question.objects.all()

    context = {
        'score' : score,
        'total' : total,
        'questions' : qs,
        'answer' : ans
    }

    return render(request, 'pages/exam.html', context)


class ExamListView(ListView):
    model = Question

    def head(self, *args, **kwargs):
        questions = self.get_queryset()
        response = HttpResponse()
        # RFC 1123 date format
        #response['Last-Modified'] = last_book.publication_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response


