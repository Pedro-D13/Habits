from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Goal
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def Home(request):
    return render(request, 'habits/index.html')


class GoalListView(LoginRequiredMixin, ListView):
    queryset = Goal.objects.filter()
    template_name = "habits/goal_list.html"
    context_object_name = "goals"

    def get_queryset(self):
        qset = Goal.objects.filter(profile__id=self.request.user.id)
        return qset


class GoalCreateView(LoginRequiredMixin, CreateView):
    model = Goal
    fields = ['goal_title', 'mantra']
    template_name = "habits/goal_createform.html"

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


class GoalUpdateView(UpdateView):
    model = Goal
    fields = ['goal_title', 'goal_status', 'mantra']


class GoalDeleteView(DeleteView):
    model = Goal
    success_url = reverse_lazy('goal_list')


# This view below is an example of how we can update the commited and practised fields in our model
# class AuthorDetailView(DetailView):

#     queryset = Author.objects.all()

#     def get_object(self):
#         obj = super().get_object()
#         # Record the last accessed date
#         obj.last_accessed = timezone.now()
#         obj.save()
#         return obj
