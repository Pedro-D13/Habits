from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TDLhead, TDLitem, TDLnotes, TDLsubtitle
# Create your views here.


class TDL_ListView(LoginRequiredMixin, ListView):
    model = TDLhead
    template_name = "todolist/tdl.html"
    context_object_name = "tdl"

    def get_queryset(self):
        ''' retrieves the queryset for that user '''
        queryset = TDLhead.objects.filter(
            profile=self.request.user.profile)
        return queryset


class TDLCreateView(LoginRequiredMixin, CreateView):
    model = TDLhead
    fields = ['header', 'completed']
    template_name = "todolist/tdl.html"
    success_url = reverse_lazy('tdl:tdl_list')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


class TDLUpdateView(LoginRequiredMixin, UpdateView):
    model = TDLhead
    fields = ['header', 'completed']
    success_url = reverse_lazy('tdl:tdl_list')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


class TDLDeleteView(LoginRequiredMixin, DeleteView):
    model = TDLhead
    success_url = reverse_lazy('tdl:tdl_list')
