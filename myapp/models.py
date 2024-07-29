# from django.db import models
# class Event(models.Model):
#     title = models.CharField(max_length=200)
#     date = models.DateField()

#     def __str__(self):
#         return self.title
    
# class UserProfile(models.Model):
#     user = models.OneToOneField(
#         'auth.User',
#         on_delete=models.CASCADE,
#         related_name='profile'
#     )
#     bio = models.TextField(blank=True)
#     # Add any additional fields you need for user profile

#     def __str__(self):
#         return self.user.username

from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    bio = models.TextField(blank=True)
    # Add any additional fields you need for user profile

    def __str__(self):
        return self.user.username
