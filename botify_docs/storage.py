import urlparse

from django.conf import settings
from django.core.files.storage import get_storage_class

from storages.backends.s3boto import S3BotoStorage

from django.contrib.staticfiles.storage import CachedFilesMixin

from pipeline.storage import PipelineMixin


class CachedS3BotoStorage(PipelineMixin, CachedFilesMixin, S3BotoStorage):
    pass


def domain(url):
    return urlparse.urlparse(url).hostname


class MediaFilesStorage(S3BotoStorage):
    def __init__(self, *args, **kwargs):
        kwargs['bucket'] = settings.AWS_STORAGE_BUCKET_NAME
        kwargs['custom_domain'] = domain(settings.MEDIA_URL)
        super(MediaFilesStorage, self).__init__(*args, **kwargs)


class StaticFilesStorage(CachedS3BotoStorage):
    def __init__(self, *args, **kwargs):
        kwargs['bucket'] = settings.AWS_STORAGE_BUCKET_NAME
        kwargs['custom_domain'] = domain(settings.STATIC_URL)
        super(StaticFilesStorage, self).__init__(*args, **kwargs)


class CompressorFilesStorage(S3BotoStorage):
    """
    S3 storage backend that saves the files locally, too.
    """
    def __init__(self, *args, **kwargs):
        kwargs['bucket'] = settings.AWS_STORAGE_BUCKET_NAME
        # kwargs['custom_domain'] = domain(settings.STATIC_URL)
        self.local_storage = get_storage_class(
            "compressor.storage.CompressorFileStorage")()

        super(CompressorFilesStorage, self).__init__(*args, **kwargs)

    def save(self, name, content):
        name = super(CompressorFilesStorage, self).save(name, content)
        self.local_storage._save(name, content)
        return name
