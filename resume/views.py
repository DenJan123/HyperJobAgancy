from django.shortcuts import render
from django.views import View
from .models import *
from .utils import VacancyForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

# Create your views here.
# class based view


class ResumeView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        return render(request, 'vacancy/show_list_objects.html',
                      context={'it_objects': resumes,
                               'message': 'resumes'})


# old way making views via view without createview

# @method_decorator(login_required, name='get')
# as it turns out you can't use here LoginRequired Mixin, you have to forbid only when anon tries to create resume
class NewResumeView(View):
    # login_url = '/login'
    def get(self, request, *args, **kwargs):
        context = {'form': VacancyForm()}
        return render(request, 'resume/resume_new.html', context=context)

    def post(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied
        form = VacancyForm(request.POST)
        if form.is_valid():
            vacancy_new = form.save(commit=False)
            vacancy_new.author = request.user
            vacancy_new.save()
            return HttpResponseRedirect(reverse('profile'))
        return render(request, 'resume/resume.new.html', {'form':form})

