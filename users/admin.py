from django.contrib import admin
from habits_tracker.models import Goal, Habit, JournalEntry
from users.models import Profile


# Register your models here.


class GoalInline(admin.StackedInline):
    model = Goal


# class HabitInline(admin.StackedInline):
#     model = Habit


# class JournalAdmin(admin.StackedInline):
#     model = JournalEntry


class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        GoalInline,
    ]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Habit)
admin.site.register(JournalEntry)
