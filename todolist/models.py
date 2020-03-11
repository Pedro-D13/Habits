from django.db import models
from datetime import datetime, timedelta
from users.models import Profile
from django.urls import reverse
from django.conf import settings
from django.utils.timezone import make_aware


def Tomorrow():
    settings.TIME_ZONE
    tmoz = datetime.today() + timedelta(days=1)
    tmoz = tmoz.replace(hour=18, minute=0, second=0, microsecond=0)
    tmoz = make_aware(tmoz)
    return tmoz


class TDlist(models.Model):
    title = models.CharField(max_length=25)
    completed = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class TDitem(models.Model):
    tdlist = models.ForeignKey(TDlist, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    duedate = models.DateTimeField(default=Tomorrow())
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.content} {self.duedate}, completed:{self.status}"

    def get_absolute_url(self):
        return reverse('tdl:tdl_detail', kwargs={'pk': self.tdlist.id})

    class Meta:
        ordering = ['duedate']


# class TDLsubtitle(models.Model):
#     item = models.ForeignKey(TDLitem, on_delete=models.CASCADE)
#     subtitle = models.CharField(max_length=100)
#     sub_status = models.BooleanField(default=False)

#     def __str__(self):
#         return self.subtitle


# class TDLnotes(models.Model):
#     item = models.ForeignKey(TDLitem, on_delete=models.CASCADE)
#     notes = models.TextField()

#     def __str__(self):
#         return self.notes
