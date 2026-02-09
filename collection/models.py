from django.db import models
from django.contrib.auth.models import User


class Patrons(models.Model):
    s_id = models.IntegerField()
    s_user = models.CharField(max_length=120)
    s_fname = models.CharField(max_length=120)
    s_lname = models.CharField(max_length=64)
    s_email = models.CharField()
    s_pass = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

