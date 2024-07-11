from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User



class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=500)
    website = models.URLField(max_length=150)
    
    def __str__(self) -> str:
        return self.name
    


class Movie(models.Model):
    title = models.CharField(max_length=1000)
    genre = models.CharField(max_length=250)
    storyline = models.CharField(max_length=500)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='movies')
    total_reviews = models.IntegerField(default=0)
    avg_rating = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    
    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    rating = models.PositiveBigIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    text = models.CharField(max_length=500)
    review_by = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.movie.title} | {self.rating}*"

