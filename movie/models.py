from django.db import models

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