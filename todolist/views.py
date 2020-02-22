from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TDLhead, TDLitem, TDLnotes, TDLsubtitle
# Create your views here.


class TDL_List(LoginRequiredMixin, ListView):
    model = TDLhead
    template_name = "todolist/tdl.html"
    context_object_name = "tdl"

    def get_queryset(self):
        ''' retrieves the queryset for that user '''
        queryset = TDLhead.objects.filter(
            profile=self.request.user.profile)
        return queryset


class TDLCreate(LoginRequiredMixin, CreateView):
    pass


class TDLUpdate(LoginRequiredMixin, UpdateView):
    pass


class TDLDelete(LoginRequiredMixin, DeleteView):
    pass
