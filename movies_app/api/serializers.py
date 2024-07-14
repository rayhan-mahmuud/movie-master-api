from movies_app.models import Movie, StreamPlatform, Review
from django.contrib.auth.models import User
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    
    review_by = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        exclude = ['movie']



class MovieSerializer(serializers.ModelSerializer):
    
    reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.StringRelatedField()
    platform_id = serializers.PrimaryKeyRelatedField(
        queryset=StreamPlatform.objects.all(),
        source='platform',
        write_only=True
    )
    
    # total_reviews = serializers.SerializerMethodField()
    # avg_rating = serializers.SerializerMethodField()
    
    class Meta:
        model = Movie
        fields = '__all__'
        
    # def get_total_reviews(self, obj):
    #     return obj.reviews.count()
    
    # def get_avg_rating(self, obj):
    #     if obj.reviews.all() is not None and obj.reviews.count()>0:
    #         ratings = [r.rating for r in obj.reviews.all()]
    #         return sum(ratings)/obj.reviews.count()
    #     else:
    #         return 0
            
        
    
    


class StreamPlatformSerializer(serializers.ModelSerializer):
    
    movies = MovieSerializer(many=True, read_only=True)
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        
    












# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     genre = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.genre = validated_data.get('genre', instance.genre)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
    
