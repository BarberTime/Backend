from minio import Minio
from django.core.files.storage import Storage
from django.conf import settings
import os

class MinioStorage(Storage):
    def __init__(self):
        self.client = Minio(
            settings.MINIO_STORAGE_ENDPOINT,
            access_key=settings.MINIO_STORAGE_ACCESS_KEY,
            secret_key=settings.MINIO_STORAGE_SECRET_KEY,
            secure=settings.MINIO_STORAGE_USE_HTTPS
        )
        self.bucket_name = settings.MINIO_STORAGE_MEDIA_BUCKET_NAME

    def _open(self, name, mode='rb'):
        try:
            response = self.client.get_object(self.bucket_name, name)
            return response
        except Exception as e:
            raise FileNotFoundError(f"Could not open file: {name}")

    def _save(self, name, content):
        try:
            content.seek(0)
            self.client.put_object(
                self.bucket_name,
                name,
                content,
                length=os.fstat(content.fileno()).st_size
            )
            return name
        except Exception as e:
            raise IOError(f"Could not save file: {name}")

    def delete(self, name):
        try:
            self.client.remove_object(self.bucket_name, name)
        except Exception as e:
            raise IOError(f"Could not delete file: {name}")

    def exists(self, name):
        try:
            self.client.stat_object(self.bucket_name, name)
            return True
        except Exception:
            return False

    def url(self, name):
        try:
            return self.client.presigned_get_object(self.bucket_name, name)
        except Exception as e:
            raise ValueError(f"Could not get URL for file: {name}")
