from django.shortcuts import render
from .models import Person, Goal, Habit, JournalEntry
from django.views.generic import TemplateView
# Create your views here.


def Home(request):
    goals = Goal.objects.all()
    habits = Habit.objects.all()
    entries = JournalEntry.objects.all()
    context = {'goals': goals, 'habits': habits, 'entries': JournalEntry}
    return render(request, 'habits/index.html', context)
