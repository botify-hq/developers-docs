import os
from django.contrib.staticfiles.finders import AppDirectoriesFinder as BaseAppDirectoriesFinder
from django.contrib.staticfiles import utils
from django.utils import six
from django.conf import settings


class AppDirectoriesFinder(BaseAppDirectoriesFinder):

    def list(self, ignore_patterns):
        """
        List all files in all app storages.
        """
        if ignore_patterns is not None:
            ignore_patterns += settings.FINDER_IGNORE_PATTERNS
        for storage in six.itervalues(self.storages):
            if storage.exists(''):  # check if storage location exists
                for path in self._get_files(storage, ignore_patterns):
                    yield path, storage

    def _get_files(self, storage, ignore_patterns=None, location=''):
        """
        Recursively walk the storage directories yielding the paths
        of all files that should be copied.
        """
        if ignore_patterns is None:
            ignore_patterns = []
        directories, files = storage.listdir(location)
        for fn in files:
            if utils.matches_patterns(fn, ignore_patterns):
                continue
            if location:
                fn = os.path.join(location, fn)
            yield fn
        for dir in directories:
            if self.match_ignored_dir('/'.join((storage.path(location), dir)), ignore_patterns):
                continue
            if location:
                dir = os.path.join(location, dir)
            for fn in self._get_files(storage, ignore_patterns, dir):
                yield fn

    def match_ignored_dir(self, path, ignore_patterns):
        for pattern in ignore_patterns:
            if pattern in path:
                return True
        return False
