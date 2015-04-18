import datetime
from django.db import models
from userprofile.models import UserProfile
# Create your models here.


class DiaryEntry(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    entry_date = models.DateField()
    whole_foods = models.IntegerField(default=0)
    processed_foods = models.IntegerField(default=0)
    notes = models.TextField()

    def __unicode__(self):
        return "%s %s" % (self.user_profile, self.entry_date)
