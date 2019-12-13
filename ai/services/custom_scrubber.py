import logging

from django.conf import settings
from django.core.management import call_command
from django.db import connections


class AbstractScrubbingService(object):
    # USER_PASSWORD is the hash of "Admin0404!"
    DEFAULT_USER_PASSWORD = 'pbkdf2_sha256$150000$i1ZI64P5GPHI$74I7aENo6mRjCZ9lkNoObJet1Qyf5sJSJev45ygqpls='

    # Overwritable values
    keep_scrubber_data = False
    pre_scrub_functions = []
    post_scrub_functions = []

    def __init__(self):
        self._logger = logging.getLogger('django_scrubber')

    def _validation(self):
        if not settings.DEBUG:
            self._logger.warning('Attention! Needs to be run in DEBUG mode!')
            return False

        if 'django_scrubber' not in settings.INSTALLED_APPS:
            self._logger.warning('Attention! django-scrubber needs to be installed!')
            return False

        return True

    def process(self):
        self._logger.info('Start scrubbing process...')

        self._logger.info('Validating setup...')
        if not self._validation():
            self._logger.warning('Aborting process!')
            return False

        # Custom pre-scrubbing
        for name in self.pre_scrub_functions:
            self._logger.info(f'Pre-Scrubbing: Calling "{name}()"...')
            method = getattr(self, name)
            method()

        self._logger.info('Scrubbing data with "scrub_data"...')
        call_command('scrub_data')

        # Custom post-scrubbing
        for name in self.post_scrub_functions:
            self._logger.info(f'Post-Scrubbing: Calling "{name}()"...')
            method = getattr(self, name)
            method()

        # Reset scrubber data to avoid huge db dumps
        if not self.keep_scrubber_data:
            self._logger.info('Scrubbing data from "scrub_data" ...')
            cursor = connections['default'].cursor()
            cursor.execute('TRUNCATE TABLE django_scrubber_fakedata;')

        self._logger.info('Scrubbing finished!')

        return True
