from django.contrib import admin
from movies_app.models import Movie, StreamPlatform, Review


admin.site.register(Movie)
admin.site.register(StreamPlatform)
admin.site.register(Review)
