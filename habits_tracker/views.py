from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Goal
from django.views.generic.edit import FormView
#  Habit, JournalEntry
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def Home(request):
    # goals = Goal.objects.all()
    # habits = Habit.objects.all()
    # entries = JournalEntry.objects.all()
    # context = {'goals': goals, 'habits': habits, 'entries': JournalEntry}
    return render(request, 'habits/index.html')


# def GoalListView(request, LoginRequiredMixin, ListView):
    # def get_queryset(self):
    #     goals = Goal.objects.all().filter(user=self.user)
    #     return render(request, 'habits/personalpage.html', {'goals': goals
    #                                                         })


class GoalListView(LoginRequiredMixin, ListView):
    queryset = Goal.objects.filter()
    template_name = "habits/goal_list.html"
    context_object_name = "goals"

    def get_queryset(self):
        qset = Goal.objects.filter(profile__id=self.request.user.id)
        return qset

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['goal'] = User.objects.filter(goal_)


class GoalCreateView(LoginRequiredMixin, CreateView):
    model = Goal
    fields = ['goal_title', 'mantra']
    template_name = "habits/goal_createform.html"

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


# This view below is an example of how we can update the commited and practised fields in our model
# class AuthorDetailView(DetailView):

#     queryset = Author.objects.all()

#     def get_object(self):
#         obj = super().get_object()
#         # Record the last accessed date
#         obj.last_accessed = timezone.now()
#         obj.save()
#         return obj
