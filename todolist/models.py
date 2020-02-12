from django.db import models

# Create your models here.


class JournalEntry(models.Model):
    tracked_date = models.DateField(unique=True)
    notes = models.TextField()

    def __str__(self):
        return f"{self.tracked_date}, {self.habit}"
