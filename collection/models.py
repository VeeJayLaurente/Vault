from django.db import models

class Patrons(models.Model):
    s_id = models.IntegerField()
    s_user = models.CharField(max_length=120)
    s_fname = models.CharField(max_length=120)
    s_lname = models.CharField(max_length=64)
    s_email = models.CharField()
    s_pass = models.IntegerField()
