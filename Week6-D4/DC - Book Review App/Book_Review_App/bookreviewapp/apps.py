from django.apps import AppConfig


class BookreviewappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookreviewapp'

    def ready(self):
        import bookreviewapp.signals
