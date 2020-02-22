from django.db import models
from datetime import datetime, timedelta
from users.models import Profile


def Tomorrow():
    tmoz = datetime.today() + timedelta(days=1)
    return tmoz.replace(hour=18, minute=0, second=0, microsecond=0)


class TDLhead(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    header = models.CharField(max_length=25)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.header


class TDLitem(models.Model):
    tdlhead = models.ForeignKey(TDLhead, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    duedate = models.DateTimeField(default=Tomorrow())
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class TDLsubtitle(models.Model):
    item = models.ForeignKey(TDLitem, on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=100)
    sub_status = models.BooleanField(default=False)

    def __str__(self):
        return self.subtitle


class TDLnotes(models.Model):
    item = models.ForeignKey(TDLitem, on_delete=models.CASCADE)
    notes = models.TextField()

    def __str__(self):
        return self.notes
