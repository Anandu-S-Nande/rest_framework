# from django.shortcuts import render
# from .models import Movie
# from django.http import JsonResponse

# # Create your views here.

# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {
#         'movies' : list(movies.values())
#     }

#     return JsonResponse(data)

# def movie_details(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         'name' : movie.name,
#         'description' : movie.description,
#         'active' : movie.active
#     }

#     return JsonResponse(data)


# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Movie
# from watchlist.api.serializers import MovieSerializer

# @api_view(['GET',])
# def movie_list(request):
#     movies = Movie.objects.all()
#     serializer = MovieSerializer(movies, many=True)
#     return Response(serializer.data) 

# def movie_details(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     serializer = MovieSerializer(movie)
#     return Response(serializer.data) 


