from django.db import models
from django.contrib.auth.models import User 

class Patron(models.Model): # Convention: Use singular name 'Patron'
    # Link this Patron to a Django User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # Using a simple string for the artwork name since your pages are static
    artwork_name = models.CharField(max_length=100) 
    image_url = models.URLField()
    page_url = models.CharField(max_length=100) # e.g., 'gogh'

    class Meta:
        unique_together = ('user', 'artwork_name') # Prevent duplicate favorites