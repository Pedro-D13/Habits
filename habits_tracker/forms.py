from django.forms import ModelForm
from django.forms import forms
from django.forms import modelformset_factory
from habits_tracker.models import *


class GoalForm(ModelForm):
    class Meta:
        model = Goal
        fields = ['goal_title', 'mantra']
