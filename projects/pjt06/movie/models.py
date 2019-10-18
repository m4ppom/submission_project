from django.db import models
from django.urls import reverse


class Movie(models.Model):
    title = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    audience = models.IntegerField()
    open_date = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=100)
    watch_grade = models.CharField(max_length=50)
    total_score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField() 
    def get_absolute_url(self):
        return reverse("movie:movie_detail", kwargs={"movie_id": self.id})


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    comment_score = models.CharField(max_length=200)
    