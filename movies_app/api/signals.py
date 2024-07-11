from django.db.models.signals import post_save, post_delete
from movies_app.models import Review
from django.dispatch import receiver


@receiver(post_save, sender=Review)
def update_review_count_on_create(sender, instance, created, **kwargs):
    if created:
        review_count = instance.movie.reviews.count()
        ratings = [r.rating for r in instance.movie.reviews.all()]
        
        instance.movie.total_reviews = review_count
        instance.movie.avg_rating = sum(ratings)/review_count
        
        instance.movie.save()
        


@receiver(post_delete, sender=Review)
def update_review_count_on_delete(sender, instance, **kwargs):
    
    review_count = instance.movie.reviews.count()
    ratings = [r.ratings for r in instance.movie.reviews.all()]
    
    instance.movie.total_reviews = review_count
    if review_count>0:
        instance.movie.avg_rating = sum(ratings)/review_count

    instance.movie.save()
    
        