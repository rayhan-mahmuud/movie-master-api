# Generated by Django 5.0.6 on 2024-06-28 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0002_streamplatform_rename_name_movie_title_movie_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='platform',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movies_app.streamplatform'),
            preserve_default=False,
        ),
    ]
