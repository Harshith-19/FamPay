import os
from celery import Celery
from dateutil import parser
from celery.utils.log import get_task_logger
import requests

Time = '2022-07-05T00:00:00Z'
YOUTUBE_DATA_API_KEY = 'AIzaSyB3vqbjC7BDe5vfkb9jiuShEKr4Fy88JEQ'
parameters = {
        'part' : 'snippet',
        'q' : 'cricket',
        'type' : 'video',
        'order' : 'date',
        'publishedAfter' : Time,
        'maxResults' : 50,
        'key' : YOUTUBE_DATA_API_KEY
    }
url = 'https://www.googleapis.com/youtube/v3/search'
# data = requests.get(url, params=parameters)
# fetched_data = data.json()['items']

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Fampay.settings")
app = Celery("Fampay")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

@app.task(bind=True)
def database_update(self):
    from backend.models import VideoDetails
    data = requests.get(url, params=parameters)
    fetched_data = data.json()['items']
    for item in fetched_data:
        if (not VideoDetails.objects.filter(video_id=item["id"]["videoId"]).exists()):
            video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            description = item["snippet"]["description"]
            published_time = item["snippet"]["publishedAt"]
            thumbnail_url_default = item["snippet"]["thumbnails"]["default"]["url"]
            thumbnail_url_medium = item["snippet"]["thumbnails"]["medium"]["url"]
            thumbnail_url_high = item["snippet"]["thumbnails"]["high"]["url"]
            details = VideoDetails.objects.create(video_id = video_id, title = title, description = description, published_time = published_time, thumbnail_url_default = thumbnail_url_default, thumbnail_url_medium = thumbnail_url_medium, thumbnail_url_high = thumbnail_url_high)
            details.save()