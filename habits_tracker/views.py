from django.shortcuts import render
from .models import *
from django.views.generic import DetailView, ListView
# Create your views here.


class PersonView(ListView):

    model = Person
    template_name = 'habits/index.html'
