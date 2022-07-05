from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('response/', views.Paginatedresponse.as_view(), name='list'),
]