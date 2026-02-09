from django.db import models
from django.contrib.auth.models import User

class Patron(models.Model): # Convention: Use singular name 'Patron'
    # Link this Patron to a Django User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Custom fields not included in the standard User model
    s_id = models.IntegerField(unique=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"