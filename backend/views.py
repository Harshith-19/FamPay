from django.shortcuts import render

# Create your views here.
def home(request):
    # global Time
    # parameters = {
    #     'part' : 'snippet',
    #     'q' : 'cricket',
    #     'type' : 'video',
    #     'order' : 'date',
    #     'publishedAfter' : Time,
    #     'maxResults' : 50,
    #     'key' : settings.YOUTUBE_DATA_API_KEY
    # }
    # url = 'https://www.googleapis.com/youtube/v3/search'
    # data = requests.get(url, params=parameters)
    # fetched_data = data.json()['items']
    # print(len(fetched_data))
    # for i in fetched_data:
    #     video_id = i["id"]["videoId"]
    #     title = i["snippet"]["title"]
    #     description = i["snippet"]["description"]
    #     published_time = i["snippet"]["publishedAt"]
    #     thumbnail_url_default = i["snippet"]["thumbnails"]["default"]["url"]
    #     thumbnail_url_medium = i["snippet"]["thumbnails"]["medium"]["url"]
    #     thumbnail_url_high = i["snippet"]["thumbnails"]["high"]["url"]
    #     details = VideoDetails.objects.create(video_id = video_id, title = title, description = description, published_time = published_time, thumbnail_url_default = thumbnail_url_default, thumbnail_url_medium = thumbnail_url_medium, thumbnail_url_high = thumbnail_url_high)
    #     details.save()
    return render(request, 'home.html')