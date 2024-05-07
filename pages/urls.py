from django.urls import path
from .views import HomePageView, AboutPageView, NavPageView

urlpatterns = [
    path('nav/', NavPageView.as_view(), name='nav'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]