from django.db import models
from datetime import datetime, timedelta
from users.models import Profile


# Create your models here.


class TDLheading(models.Model):
    header = models.CharField(max_length=25)

    def __str__(self):
        return self.header


def Tomorrow():
    tmoz = datetime.today() + timedelta(days=1)
    return tmoz.replace(hour=18, minute=0, second=0, microsecond=0)


class TDL(models.Model):
    heading = models.OneToOneField(TDLheading, models.CASCADE)
    profile = models.ForeignKey(Profile, models.CASCADE)
    title = models.CharField(max_length=25)
    duedate = models.DateTimeField(default=Tomorrow())

    def __str__(self):
        return f"{self.title}\n Due @ {self.duedate}"


class TodoListitem(models.Model):
    node = models.ForeignKey(TDL, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    notes = models.TextField()
