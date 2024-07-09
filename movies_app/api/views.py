from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.exceptions import ValidationError
# from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework import status
from movies_app.models import Movie, StreamPlatform, Review
from movies_app.api.serializers import MovieSerializer, StreamPlatformSerializer, ReviewSerializer



class MovieListAV(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        

class MovieDetailsAV(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#-------------------------------------------------------------------------------------------------------------------

class StreamingListAV(mixins.ListModelMixin, 
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    


class StreamingDetailAV(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
#-------------------------------------------------------------------------------------------------------------------    

class ReviewListAV(generics.ListAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        movie = Movie.objects.get(pk=pk)
        queryset = Review.objects.filter(movie=movie)
        if queryset.exists():
            return queryset
    
    
class ReviewCreateAV(generics.CreateAPIView):

    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = Movie.objects.get(pk=pk)
        
        review_by = self.request.user
        movie_query = Review.objects.filter(movie=movie, review_by=review_by)
        if movie_query.exists():
            raise ValidationError("This user already given a review for this movie!")
        
        serializer.save(movie=movie, review_by=review_by)
    
    
class ReviewDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_object(self):
        pk = self.kwargs.get('review_id')
        return Review.objects.get(pk=pk)

#-------------------------------------------------------------------------------------------------------------------


# class StreamingListAV(APIView):
#     def get(self, request):
#         streaming_list = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(streaming_list, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        

# class StreamingDetailAV(APIView):
#     def get(self, request, pk):
#         streaming = StreamPlatform.objects.get(pk=pk)
#         serializer = StreamPlatformSerializer(streaming)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         streaming = StreamPlatform.objects.get(pk=pk)
#         serializer = StreamPlatformSerializer(streaming, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
    
#     def delete(self, request, pk):
#         streaming = StreamPlatform.objects.get(pk=pk)
#         streaming.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)











# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error': 'Movie with this id does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error': 'Movie with this id does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
        
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
        
