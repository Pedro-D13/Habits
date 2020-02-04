from django.shortcuts import render
from .models import Goal, Habit, JournalEntry
from django.views.generic import TemplateView, CreateView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def Home(request):
    goals = Goal.objects.all()
    habits = Habit.objects.all()
    entries = JournalEntry.objects.all()
    context = {'goals': goals, 'habits': habits, 'entries': JournalEntry}
    return render(request, 'habits/index.html', context)


class GoalListView(LoginRequiredMixin, ListView):
    model = Goal
    template_name = "habits/personalpage.html"

    # def get_queryset(self):
    #     goals = Goal.objects.all().filter(user=self.user)
    #     return render(request, 'habits/personalpage.html', {'goals': goals
    #                                                         })


class GoalCreateView(LoginRequiredMixin, CreateView):
    model = Goal
    fields = ['goal_desc', 'mantra']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
