from django.urls import path
from movies_app.api import views

urlpatterns = [
    path('movies/', views.MovieListAV.as_view(), name='movie_list'),
    path('movies/<int:pk>/', views.MovieDetailsAV.as_view(), name='movie_detail'),
    
    path('movies/<int:pk>/reviews-create/', views.ReviewCreateAV.as_view(), name='review_create'),
    path('movies/<int:pk>/reviews/', views.ReviewListAV.as_view(), name='review_list'),
    path('movies/<int:pk>/reviews/<int:review_id>/', views.ReviewDetailAV.as_view(), name='review_detail'),
    
    path('streaming/', views.StreamingListAV.as_view(), name='streaming_list'),
    path('streaming/<int:pk>/', views.StreamingDetailAV.as_view(), name='streaming_detail'),
    
]
