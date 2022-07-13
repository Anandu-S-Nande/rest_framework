from django.urls import path 
from watchlist.api.views import movie_details , movie_list
#from . import views

urlpatterns = [
    path('list/', movie_list, name="movie_list"),
    path('<int:pk>', movie_details, name="movie_deatils"),
]

# from django.urls import path
# #from watchlist.views import movie_list , movie_details
# from .views import movie_details, movie_list

# urlpatterns = [
#     path('list/', movie_list, name="movie_list"),
#     path('<int:pk>',movie_details, name="movie_deatils"),
# ]
