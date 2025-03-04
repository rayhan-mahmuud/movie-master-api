# Generated by Django 5.0.6 on 2024-07-11 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0005_review_review_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='avg_rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='movie',
            name='total_reviews',
            field=models.IntegerField(default=0),
        ),
    ]
