#from rest_framework.decorators import api_view
from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from watchlist.models import WatchList , StreamPlatform , Review
from .serializers import WatchListSerializer , StreamPlatformSerializer , ReviewSerializer
from rest_framework import status
from rest_framework import generics
#from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly 

from .permissions import AdminOrReadOnly ,  ReviewUserOrReadOnly


##################################### CONCREATE VIEW ######################################################################

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist =  WatchList.objects.get(pk=pk)
 
       ################ user check 1 user can 1 review #######################
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, review_user=review_user)

        if review_queryset.exists():
            raise ValidationError("you have already reviewed this movie")

        ################## Caluclate the rating ######################################

        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = ( watchlist.avg_rating + serializer.validated_data['rating'])/2

        watchlist.number_rating = watchlist.number_rating  + 1
        watchlist.save()

        serializer.save(watchlist=watchlist, review_user=review_user)
        

class ReviewList(generics.ListAPIView):
    #queryset = Review.objects.all() 
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated] # base authentication
    #permission_classes = [IsAuthenticatedOrReadOnly] # permission in class like each objects level
    #permission_classes = [ReviewUserOrReadOnly] coustom permission class

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadOnly] # permission in class like each objects level


###################################### CONCREATE VIEW ##########################################################################################

# class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
     
     #we cannnot write get , post etc methods.

################################### GENRIC APIView(MIXINS) ########################################################################

# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
   


# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin,  generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)  ## it is an another method of views. use mixins we can create get post methods easily   

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

########################################## CLASS BASE VIEW ###############################################################################

class WatchListAV(APIView):

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True) ### GET method
        return Response(serializer.data) 

    def post(self, request):
        serializer = WatchListSerializer(data=request.data) #### POST Method
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailAV(APIView):

    def get(self, request, pk):
        try:
           movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error' : 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializer(movie) ##### GET method
        return Response(serializer.data) 

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data) #### PUT method
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)  ### DELETE method
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#################################### MODEL VIEW SET ####################################################################

class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class =  StreamPlatformSerializer




############################ VIEWSET & ROUTERS ##############################################################

# class StreamPlatformVS(viewsets.ViewSet):

#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer =  StreamPlatformSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(watchlist)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#         else:
#            return Response(serializer.errors)


####################################### CLASS BASE ###################################################################



class StreamPlatformAV(APIView):

    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        else:
           return Response(serializer.errors)

class StreamPlatformDetailsAV(APIView):

    def get(self, request, pk):
        try:
           platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error' : 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializer(platform) ##### GET method
        return Response(serializer.data) 
    
    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data) #### PUT method
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    def delete(self, request, pk):
        movie = StreamPlatform.objects.get(pk=pk)  ### DELETE method
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


########################################## FUNCTION BASE ###############################################################################


# @api_view(['GET', 'POST'])
# def movie_list(request):

#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data) 
    
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data) #### POST Method
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET', 'PUT','DELETE'])
# def movie_details(request, pk):

#     if request.method == 'GET':
#         try:
#            movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error' : 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = MovieSerializer(movie) ##### GET method
#         return Response(serializer.data) 

#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data) #### PUT method
#         if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)  ### DELETE method
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
