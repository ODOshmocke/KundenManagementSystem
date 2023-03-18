from django.apps import AppConfig
from .schedulers import start_checking_emails

class RegisterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'register'

    def ready(self):
        start_checking_emails()
