from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.


class SignUp(models.Model):
    first_name = models.CharField(max_length=80, null=True, blank=True)
    last_name = models.CharField(max_length=80, null=True, blank=True)
    email = models.EmailField()

    def get_absolute_url(self):
        return "/%s" % self.last_name

    def __unicode__(self):
        return self.email


