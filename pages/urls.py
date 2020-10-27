from django.urls import path

from .views import HomePageView, AboutPageView, ResultPageView, ToppersPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('result/', ResultPageView.as_view(), name='result'),
    path('toppers/', ToppersPageView.as_view(), name='toppers'),
]
