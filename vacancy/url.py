from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name='index'),
    path("home", home, name='profile'),
    path("vacancies/", VacanciesView.as_view(), name='vacancies'),
    path('login', MyLoginView.as_view(), name='login'),
    path('logout', MyLogoutView.as_view()),
    path('signup', SignupView.as_view()),
    path('vacancy/new', NewVacancyView.as_view(), name='vacancy_new')
]
