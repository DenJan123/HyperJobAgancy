from django.shortcuts import render
from django.views import View
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .utils import VacancyForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from resume.views import NewResumeView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden

def index(request):
    return render(request, "vacancy/index.html")

# class based view
class VacanciesView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        return render(request, 'vacancy/show_list_objects.html',
                      context={'it_objects': vacancies,
                               'message': 'vacancies'})


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'vacancy/signup.html'


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    success_url = '/'
    template_name = 'vacancy/login.html'


class MyLogoutView(LogoutView):
    pass


# modern way to do a view
# class NewVacancyView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
class NewVacancyView(CreateView):
    # permission_required = 'user.profile.is_staff'
    # raise_exception = False
    # login_url = '/login'
    success_url = '/home'
    template_name = 'vacancy/vacancy_new.html'
    model = Vacancy
    fields = ['description']

    def form_valid(self, form):
        # if self.request.user.is_anonymous:
        #     raise PermissionDenied
        form.instance.author = self.request.user
        if not self.request.user.profile.is_staff:
            # raise PermissionDenied
            return HttpResponseForbidden()
        return super().form_valid(form)

    def post(self, request, **kwargs):
        if self.request.user.is_anonymous:
            return HttpResponseForbidden()
        return super().post(request, **kwargs)

def home(request):
    if request.user.is_anonymous:
        return NewResumeView.as_view()(request)
    elif request.user.profile.is_staff:
        return NewVacancyView.as_view()(request)
    else:
        return NewResumeView.as_view()(request)


"""As it turns out you can't use any "raise exception" in your code, even though your code is working, you won't be able to pass the test.  """
