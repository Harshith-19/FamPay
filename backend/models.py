from django.db import models

# Create your models here.
class VideoDetails(models.Model):
    video_id = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    published_time = models.CharField(max_length = 100)
    thumbnail_url_default = models.CharField(max_length = 100)
    thumbnail_url_medium = models.CharField(max_length = 100)
    thumbnail_url_high = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.published_time)
    class Meta:
       ordering = ('-published_time',)