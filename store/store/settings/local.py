from django.conf import settings
from .base import *

settings.DEBUG = True
# E-Mail settings
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
