from storages.backends.s3boto3 import S3BotoStorage as S3BotoStorageOriginal
from django.contrib.staticfiles.storage import ManifestFilesMixin


class S3BotoStorage(S3BotoStorageOriginal):
    class ManifestS3Storage(ManifestFilesMixin, S3BotoStorage):
        pass
