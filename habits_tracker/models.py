import datetime as dt

from django.db import models
from django.contrib.auth.models import User
# from django.db.models import Case, Value, When
from datetime import date, timedelta
from users.models import Profile
# Create your models here.


GOAL_CHECKBOX = [
    ('TS', 'To start'),
    ('PR', 'progressing'),
    ('AC', 'Achieved'),
]


class Goal(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    goal_title = models.CharField(max_length=25)
    goal_status = models.CharField(choices=GOAL_CHECKBOX, max_length=20)
    mantra = models.TextField()

    def __str__(self):
        return f"{self.goal_title}:{self.goal_status}"

    # #     def get_absolute_url(self):
    # #         return reverse("model_detail", kwargs={"pk": self.pk})


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


# class JournalEntry(models.Model):
#     habit = models.ForeignKey(
#         Habit, on_delete=models.CASCADE, primary_key=True)
#     tracked_date = models.DateField(unique=True)
#     notes = models.TextField()

#     def __str__(self):
#         return f"{self.tracked_date}, {self.habit}"
