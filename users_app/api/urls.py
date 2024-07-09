from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users_app.api import views

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', views.UserRegistrationGV.as_view(), name='register'),
    path('logout/', views.LogOutAV.as_view(), name='logout'),
]
