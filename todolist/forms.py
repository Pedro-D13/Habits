from django.forms import ModelForm
from django.forms import forms
from django.forms import modelformset_factory
from todolist.models import *


class TDLForm(ModelForm):

    class Meta:
        model = TDLhead
        fields = ['header', 'completed']
