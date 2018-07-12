from django.db import models
from django.contrib.auth.models import User as SuperUser

class User(SuperUser):

    def __str__(self):
        return str(self.username)

    def __unicode__(self):
        return str(self.username)