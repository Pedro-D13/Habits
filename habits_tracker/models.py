import datetime as dt

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Case, Value, When
from datetime import date, timedelta

# Create your models here.


class Person(models.Model):
    f_name = models.CharField(max_length=40)
    l_name = models.CharField(max_length=40)
    age = models.SmallIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.f_name}, {self.l_name} {self.age}"

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})


class Goal(models.Model):
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, primary_key=True,)
    goal_desc = models.CharField(max_length=100)
    mantra = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"{self.goal_desc}, by {self.person}"


class Habit(models.Model):
    habit_title = models.CharField(max_length=40, unique=True)
    habit_desc = models.CharField(max_length=200)
    preparations = models.TextField(blank=True)
    commited = models.BooleanField(default=False)
    goal = models.ForeignKey(
        Goal, on_delete=models.CASCADE)
    practised_today = models.DateField()

    def __str__(self):
        return f"{self.habit_title} to achieve {self.goal}"


class JournalEntry(models.Model):
    habit = models.ForeignKey(
        Habit, on_delete=models.CASCADE)
    tracked_date = models.DateField(unique=True)
    notes = models.TextField()

    def __str__(self):
        return f"{self.tracked_date}, {self.habit}"
