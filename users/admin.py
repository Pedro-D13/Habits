from django.contrib import admin
from habits_tracker.models import Goal
# Habit, JournalEntry
from users.models import Profile


# Register your models here.


# class HabitInline(admin.StackedInline):
#     model = Habit


# class JournalAdmin(admin.StackedInline):
#     model = JournalEntry


admin.site.register(Profile)
admin.site.register(Goal)
# admin.site.register(Habit)
# admin.site.register(JournalEntry)
