from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Goal
from .forms import GoalForm
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_http_methods
# Create your views here.


def Home(request):
    return render(request, 'habits/index.html')


class GoalListView(LoginRequiredMixin, ListView):
    queryset = Goal.objects.filter()
    template_name = "habits/goal_list.html"
    context_object_name = "goals"
    success_url = 'habits/goal_list.html'

    def post(self, request, *args, **kwargs):
        request.POST['goal_title']

    # def get_queryset(self):
    #     qset = Goal.objects.filter(profile__id=self.request.user.id)
    #     return qset


class GoalCreateView(LoginRequiredMixin, CreateView):
    model = Goal
    fields = ['goal_title', 'mantra']
    template_name = "habits/goal_createform.html"
    success_url = reverse_lazy('habits:goal_list')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


class GoalDetailView(LoginRequiredMixin, DeleteView):
    model = Goal
    template_name = 'habits/goal_detail.html'
    context_object_name = 'goal'
    success_url = 'habits/goal_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["goal_detail"] = Goal.objects.all()
        return context


class GoalUpdateView(LoginRequiredMixin, UpdateView):
    model = Goal
    fields = ['goal_title', 'mantra']
    success_url = reverse_lazy('habits:goal_list')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


# @require_http_methods(["POST"])
# def GoalUpdateView(request, goal_id):
#     to_update = get_object_or_404(Goal, pk=goal_id)
#     if request.user.profile == to_update.profile:


#     goal_title_to_update = User.Profile.goal_set.get(
#         pk=request.POST['goal_title'])
#     goal_mantra_to_update = User.Profile.goal_set.get(
#         pk=request.POST['mantra'])
#     to_update.goal_title = goal_title
#     selected_choice.save()
#     # Always return an HttpResponseRedirect after successfully dealing
#     # with POST data. This prevents data from being posted twice if a
#     # user hits the Back button.
#     return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

    # try:

    # except (KeyError, Goal.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'goal/list.html', {
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:


class GoalDeleteView(LoginRequiredMixin, DeleteView):
    model = Goal
    success_url = reverse_lazy('habits:goal_list')


# This view below is an example of how we can update the commited and practised fields in our model
# class AuthorDetailView(DetailView):

#     queryset = Author.objects.all()

#     def get_object(self):
#         obj = super().get_object()
#         # Record the last accessed date
#         obj.last_accessed = timezone.now()
#         obj.save()
#         return obj
