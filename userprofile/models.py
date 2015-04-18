from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=80, null=True, blank=True)
    last_name = models.CharField(max_length=80, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), default='F')
    age = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)

    def __unicode__(self):
        return "%s's profile" % self.user.username

User.profile = property(lambda u: UserProfile.objects.get_or_create (user=u)[0])