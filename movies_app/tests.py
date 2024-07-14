from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from movies_app.models import StreamPlatform, Movie, Review

#Test StreamingPlatform Endpoints
#---------------------------------------------------------------------------------------------------------
class StreamPlatformTestsNoAuth(APITestCase):
    
    def setUp(self):
        self.platform = StreamPlatform.objects.create(
            name='Test Platform',
            about='For Test',
            website='https://www.test.com'                    
            )
    
    def test_platform_create(self):
        data = {
            'name': 'Test Platform',
            'about': 'This is for test',
            'website': 'https://www.test.com'
        }
        response = self.client.post(reverse('streaming_list'), data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_platform_get_list(self):
        response = self.client.get(reverse('streaming_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_platform_get_detail(self):
        response = self.client.get(reverse('streaming_detail', args=(self.platform.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_platform_put(self):
        data = {
            'name': 'Test',
            'about': 'This is for test',
            'website': 'https://www.test.com'
        }
        response = self.client.put(reverse('streaming_detail', args=(self.platform.id,)), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    
    def test_platform_delete(self):
        response = self.client.delete(reverse('streaming_detail', args=(self.platform.id,)))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)



class StreamPlatformTestsAuth(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass12345')
        data={
            'username':'testuser',
            'password':'testpass12345'
        }
        response = self.client.post(reverse('login'), data)
        self.token = Token.objects.get(user__username='testuser')
        
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)
        
        self.platform = StreamPlatform.objects.create(
            name='Test Platform 1',
            about='For Test',
            website='https://www.test.com'                    
            )
    
    def test_platform_create(self):
        data = {
            'name': 'Test Platform 2',
            'about': 'This is for test',
            'website': 'https://www.test.com'
        }
        response = self.client.post(reverse('streaming_list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_platform_get_list(self):
        response = self.client.get(reverse('streaming_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_platform_get_detail(self):
        response = self.client.get(reverse('streaming_detail', args=(self.platform.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_platform_put(self):
        data = {
            'name': 'Test',
            'about': 'This is for test',
            'website': 'https://www.test.com'
        }
        response = self.client.put(reverse('streaming_detail', args=(self.platform.id,)), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    
    def test_platform_delete(self):
        response = self.client.delete(reverse('streaming_detail', args=(self.platform.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        

#Test Movie Endpoints
#--------------------------------------------------------------------------------------------

class MovieTestsNoAuth(APITestCase):
    
    def setUp(self):
        self.platform = StreamPlatform.objects.create(
            name='Test Platform',
            about='For Test',
            website='https://www.test.com'                   
            )
        
        self.movie = Movie.objects.create(
            title='Test Movie',
            genre='Test',
            storyline='This is a test movie',
            platform_id=self.platform.id,
            active=True
        )
        
    def test_movie_create(self):
        data={
            "title": "New Test",
            "genre": "Test",
            "storyline": "Test movie",
            "active": True,
            "platform_id": self.platform.id
        }
        response = self.client.post(reverse('movie_list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_movie_get_list(self):
        response = self.client.get(reverse('movie_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_movie_get_detail(self):
        response = self.client.get(reverse('movie_detail', args=(self.movie.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_movie_put(self):
        data={
            "title": "New Test Updated",
            "genre": "Test Updated",
            "storyline": "Test movie",
            "active": True,
            "platform_id": self.platform.id
        }
        response = self.client.put(reverse('movie_detail', args=(self.movie.id,)), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_movie_delete(self):
        response = self.client.delete(reverse('movie_detail', args=(self.movie.id,)))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    

class MovieTestsWithAuth(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass12345')
        data={
            'username':'testuser',
            'password':'testpass12345'
        }
        response = self.client.post(reverse('login'), data)
        self.token = Token.objects.get(user__username='testuser')
        
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)
        
        self.platform = StreamPlatform.objects.create(
            name='Test Platform',
            about='For Test',
            website='https://www.test.com'                   
            )
        
        self.movie = Movie.objects.create(
            title='Test Movie',
            genre='Test',
            storyline='This is a test movie',
            platform_id=self.platform.id,
            active=True
        )
        
    def test_movie_create(self):
        data={
            "title": "New Test",
            "genre": "Test",
            "storyline": "Test movie",
            "active": True,
            "platform_id": self.platform.id
        }
        response = self.client.post(reverse('movie_list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_movie_get_list(self):
        response = self.client.get(reverse('movie_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_movie_get_detail(self):
        response = self.client.get(reverse('movie_detail', args=(self.movie.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_movie_put(self):
        data={
            "title": "New Test Updated",
            "genre": "Test Updated",
            "storyline": "Test movie",
            "active": True,
            "platform_id": self.platform.id
        }
        response = self.client.put(reverse('movie_detail', args=(self.movie.id,)), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_movie_delete(self):
        response = self.client.delete(reverse('movie_detail', args=(self.movie.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        

#Test Review Endpoints
#--------------------------------------------------------------------------------------------------------------------
class ReviewTests(APITestCase):
    
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='testuser', password='testpass12345')
        self.user2 = User.objects.create_user(username='testuser2', password='testpass12345')
        data={
            'username':'testuser',
            'password':'testpass12345'
        }
        response = self.client.post(reverse('login'), data)
        self.token = Token.objects.get(user__username='testuser')
        
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)
        
        self.platform = StreamPlatform.objects.create(
            name='Test Platform',
            about='For Test',
            website='https://www.test.com'                   
            )
        
        self.movie = Movie.objects.create(
            title='Test Movie',
            genre='Test',
            storyline='This is a test movie',
            platform_id=self.platform.id,
            active=True
        )
        
        self.review = Review.objects.create(
            rating=5,
            text="This is a review for testing",
            movie=self.movie,
            review_by = self.user2
        )
        
    def test_review_create(self):
        data = {
            "rating": 5,
            "text": "Test Review"
        }
        response = self.client.post(reverse('review_create', args=(self.movie.id,)), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        response = self.client.post(reverse('review_create', args=(self.movie.id,)), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        
    def test_review_create_unauth(self):
        data = {
            "rating": 5,
            "text": "Test Review"
        }
        self.client.force_authenticate(user=None)
        response = self.client.post(reverse('review_create', args=(self.movie.id,)), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_review_get_list(self):
        response = self.client.get(reverse('review_list', args=(self.movie.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        #For unauthenticated user
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse('review_list', args=(self.movie.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    
    def test_review_get_detail(self):
        response = self.client.get(reverse('review_detail', args=(self.movie.id, self.review.id)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        #For unauthenticated user
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse('review_detail', args=(self.movie.id, self.review.id)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    
    def test_review_put(self):
        data = {
            "rating": 4,
            "text": "Test Review"
        }
        response = self.client.put(reverse('review_detail', args=(self.movie.id, self.review.id)), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        #For unauthenticated user
        self.client.force_authenticate(user=None)
        response = self.client.put(reverse('review_detail', args=(self.movie.id, self.review.id)), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        
    def test_review_delete(self):
        response = self.client.delete(reverse('review_detail', args=(self.movie.id, self.review.id)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        #For unauthenticated user
        self.client.force_authenticate(user=None)
        response = self.client.delete(reverse('review_detail', args=(self.movie.id, self.review.id)))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    




