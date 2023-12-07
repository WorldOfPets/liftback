from django.apps import AppConfig
from django.db.models.signals import post_migrate



class LiftsConfig(AppConfig):
    name = 'lifts_app'
    verbose_name = "Главное"
    def ready(self):
        from lifts_app.signals import test_data
        post_migrate.connect(test_data, sender=self)
        #import lifts_app.signals
        