from django.contrib import admin
from .models import Person, Goal, Habit, JournalEntry
# Register your models here.


class GoalInline(admin.TabularInline):
    model = Goal


class PersonAdmin(admin.ModelAdmin):
    inlines = [
        GoalInline,
    ]


admin.site.register(Person, PersonAdmin)
