
import datetime as dt
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
# from django.db.models import Case, Value, When
from datetime import date, timedelta
from users.models import Profile
# Create your models here.


class Goal(models.Model):
    TS = 'To Start'
    PR = 'In Progress'
    AC = 'Achieved'
    GoalCheckBox = [
        (TS, 'To Start'),
        (PR, 'In Progress'),
        (AC, 'Achieved')
    ]
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    goal_title = models.CharField(max_length=25)
    goal_status = models.CharField(
        choices=GoalCheckBox,
        default=TS,
        max_length=11)
    mantra = models.TextField()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.goal_title} {self.goal_status}"

    def get_absolute_url(self):
        return reverse("goal_detail", kwargs={"pk": self.pk})


class Habit(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    habit_title = models.CharField(max_length=40)
    notes = models.TextField(null=True, default='')

    def __str__(self):
        return f"{self.habit_title} to achieve {self.goal}, {self.goal.profile}"

    # class Habit(models.Model):
    #     goal = models.ForeignKey(
    #         Goal, on_delete=models.CASCADE,  primary_key=True)
    #     habit_title = models.CharField(
    #         max_length=40, unique=True)
    #     habit_desc = models.CharField(max_length=200)
    #     preparations = models.TextField(blank=True)
    #     commited = models.BooleanField(default=False)
    #     practised_today = models.DateField()
