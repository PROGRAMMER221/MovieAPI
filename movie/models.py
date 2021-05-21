from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField(max_length=500)
    rating = models.IntegerField(default=0)
    no_of_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.movie_name

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
