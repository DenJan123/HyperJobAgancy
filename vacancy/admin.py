from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Vacancy)
admin.site.register(Profile)
