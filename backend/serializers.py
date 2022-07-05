from rest_framework import serializers
from .models import VideoDetails

class VideoDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoDetails
        fields = ['video_id', 'title', 'description', 'published_time', 'thumbnail_url_default', 'thumbnail_url_medium', 'thumbnail_url_high']