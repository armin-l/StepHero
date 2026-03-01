from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    steps = models.IntegerField(default=0)

class Group(models.Model):
    name = models.CharField(max_length=255)
    invite_code = models.CharField(max_length=6, unique=True)
    members = models.ManyToManyField('User', related_name='user_groups')

    def __str__(self):
        return self.name