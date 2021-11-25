from django.urls import path
from .views import *

urlpatterns = [
    path("resumes/", ResumeView.as_view(), name='resumes'),
    path("resume/new", NewResumeView.as_view(), name='resume_new')
]
