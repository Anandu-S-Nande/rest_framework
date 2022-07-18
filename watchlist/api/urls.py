from django.urls import path 
#from watchlist.api.views import movie_details , movie_list
from watchlist.api.views import WatchListAV , WatchDetailAV , StreamPlatformAV , StreamPlatformDetailsAV
#from . import views

urlpatterns = [
    path('list/', WatchListAV.as_view(), name="movie-list"),
    path('<int:pk>', WatchDetailAV.as_view(), name="movie-deatils"), ### THis is class base url
    path('stream/', StreamPlatformAV.as_view(), name="stream-list"),
    path('stream/<int:pk>', StreamPlatformDetailsAV.as_view(), name="stream-deatils"),
    
]

# from django.urls import path
# #from watchlist.views import movie_list , movie_details
# from .views import movie_details, movie_list

# urlpatterns = [
#     path('list/', movie_list, name="movie_list"),          ###This is fucntion base url
#     path('<int:pk>',movie_details, name="movie_deatils"),
# ]

