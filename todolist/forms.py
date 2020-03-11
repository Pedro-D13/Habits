from django.forms import ModelForm
from django.forms import forms
from django.forms import modelformset_factory
from todolist.models import *


class TDListForm(ModelForm):

    class Meta:
        model = TDlist
        fields = ['title', 'completed']


class TDItemForm(ModelForm):

    class Meta:
        model = TDitem
        fields = ['tdlist', 'content', 'duedate', 'status']
