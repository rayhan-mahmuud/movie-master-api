from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from users_app.api.serializers import UserSerializer



class UserRegistrationGV(generics.CreateAPIView):
    serializer_class = UserSerializer
    

class LogOutAV(APIView):
    
    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({'logout':'successfull'})
    
    

    