from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'type': 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs={
            'password': {"write_only": True},
        }
    
    def create(self, validated_data):
        
        p1 = validated_data['password']
        p2 = validated_data['password2']
        
        email = validated_data['email']
        
        if p1 != p2:
            raise serializers.ValidationError("Both paswords needs to be same!")
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("User with this email already exists!")
        
        account = User(
            username=validated_data['username'],
            email=email
            )
        account.set_password(validated_data['password'])
        account.save()
        
        return account
        
