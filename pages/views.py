from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class ResultPageView(TemplateView):
    template_name = 'pages/result.html'

class ToppersPageView(TemplateView):
    template_name = 'pages/toppers.html'