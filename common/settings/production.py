from project.settings.base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[DjangoIntegration()],
)

ALLOWED_HOSTS = ["127.0.0.1", "localhost",]

INSTALLED_APPS += ["storages"]

# Storage location
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "common.storage.S3BotoStorage"

STATIC_URL = "https://%s/" % (DO_SPACE_ENDPOINT)
