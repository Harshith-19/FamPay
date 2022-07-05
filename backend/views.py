from django.shortcuts import render
from .models import VideoDetails
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from .serializers import VideoDetailsSerializer

# Create your views here.
def home(request):
    return render(request, 'home.html')

class Paginatedresponse(ListAPIView):
    queryset = VideoDetails.objects.all()
    serializer_class = VideoDetailsSerializer
    pagination_class = PageNumberPagination