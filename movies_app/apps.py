from django.apps import AppConfig


class MoviesAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movies_app'
    
    def ready(self):
        import movies_app.api.signals
