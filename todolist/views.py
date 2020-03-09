from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView, DetailView
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy, reverse, resolve
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TDlist, TDitem
from django.http import Http404

# Create your views here.


class TDL_ListView(LoginRequiredMixin, ListView):
    model = TDlist
    template_name = "todolist/tdl.html"
    context_object_name = 'lists'

    def get_queryset(self):
        ''' retrieves the queryset for that user '''
        user = self.request.user
        all_lists = TDlist.objects.all()
        return all_lists.filter(profile=user.profile)


class TDLItemsListView(ListView):
    template_name = 'todolist/tdl_detail.html'
    model = TDlist
    context_object_name = 'item'

    def get_queryset(self):
        list_in_focus = TDlist.objects.get(pk=self.kwargs['pk'])
        list_to_return = list_in_focus.tditem_set.all()
        return list_to_return

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        list_in_focus = TDlist.objects.get(pk=self.kwargs['pk'])
        context['list_in_focus'] = list_in_focus
        return context


class TDL_CreateView(LoginRequiredMixin, CreateView):
    model = TDlist
    fields = ['title', 'completed']
    template_name = "todolist/tdl.html"
    success_url = reverse_lazy('tdl:tdl_list')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


class TDL_UpdateView(LoginRequiredMixin, UpdateView):
    model = TDlist
    fields = ['title', 'completed']
    success_url = reverse_lazy('tdl:tdl_list')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


class TDL_DeleteView(LoginRequiredMixin, DeleteView):
    model = TDlist
    success_url = reverse_lazy('tdl:tdl_list')


# ***** ToDoItems  **********
class TDItem_ListView(LoginRequiredMixin, ListView):
    model = TDitem
    template_name = 'todolist/tditem_list.html'

    def get_context_data(self, **kwargs):
        list_in_focus = self.kwargs['pk']
        list_items = TDitem.objects.filter(tdlist=list_in_focus)
        return {'items': list_items, 'list_in_focus': list_in_focus}


class TDLItems_CreateView(LoginRequiredMixin, CreateView):
    model = TDitem
    fields = ['tdlist', 'content', 'duedate']
    template_name = 'todolist/tdl_detail.html'

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


class TDLItems_DeleteView(LoginRequiredMixin, DeleteView):
    model = TDitem
    success_url = "/tdl/{tdlist_id}/"
