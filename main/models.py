from django.db import models

# Create your models here.
class YoutubeVideo(models.Model):
    title = models.CharField(max_length=200)
    thumbnail_url = models.URLField()
    url = models.URLField(default="https://www.youtube.com/watch?v=jNQXAC9IVRw")

    def __str__(self):
        return self.title