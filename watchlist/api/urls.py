from django.urls import path , include
#from watchlist.api.views import movie_details , movie_list
from watchlist.api.views import (WatchListAV , WatchDetailAV , StreamPlatformAV , StreamPlatformDetailsAV ,
                                  ReviewList , ReviewDetail, ReviewCreate, StreamPlatformVS)
#from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')


urlpatterns = [
    path('list/', WatchListAV.as_view(), name="movie-list"),
    path('<int:pk>', WatchDetailAV.as_view(), name="movie-deatils"), ### THis is class base url

    path('', include(router.urls)),

    #path('stream/', StreamPlatformAV.as_view(), name="stream-list"),
    #path('stream/<int:pk>', StreamPlatformDetailsAV.as_view(), name="stream-deatils"),

    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name="review-create"), #eg amazon review page
    path('stream/<int:pk>/review', ReviewList.as_view(), name="review-list"),
    path('stream/review/<int:pk>',  ReviewDetail.as_view(), name="review-detail"),
    


    # path('review',  ReviewList.as_view(), name="review-list"),
    # path('review/<int:pk>',  ReviewDetail.as_view(), name="review-detail"),
    
]

# from django.urls import path
# #from watchlist.views import movie_list , movie_details
# from .views import movie_details, movie_list

# urlpatterns = [
#     path('list/', movie_list, name="movie_list"),          ###This is fucntion base url
#     path('<int:pk>',movie_details, name="movie_deatils"),
# ]

