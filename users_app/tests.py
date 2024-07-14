from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import reverse

from django.contrib.auth.models import User


class RegisterTests(APITestCase):
    
    def test_user_registration(self):
        
        data = {
            'username': 'testcaseuser',
            'email': 'test@example.com',
            'password': 'testpass12345',
            'password2': 'testpass12345',
        }
        
        response = self.client.post(reverse('register'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
class LoginLogoutTests(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testcaseuser', 
                                             password='testpass12345')
        
    def test_login(self):
        
        data = {
            'username':'testcaseuser', 
            'password':'testpass12345'
        }
        response = self.client.post(reverse('login'), data, format='json')
        token = Token.objects.get(user__username='testcaseuser')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(token)
        
    def test_login_with_wrong_password(self):
        data = {
            'username':'testcaseuser', 
            'password':'testpass123456'
        }
        response = self.client.post(reverse('login'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    
        
    def test_logout(self):
        data = {
            'username':'testcaseuser', 
            'password':'testpass12345'
        }
        self.client.post(reverse('login'), data, format='json')
        self.token = Token.objects.get(user__username='testcaseuser')
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token.key)
        
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
        
        