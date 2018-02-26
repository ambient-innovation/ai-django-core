# -*- coding: utf-8 -*-
from django.core.files.storage import FileSystemStorage

from ai.utils.antivirus import AVException
from .scanner import AVScanner

av_scanner = AVScanner()


class AVFileSystemStorage(FileSystemStorage):
    parallel = True
    def save(self, name, content, max_length=None):
        av_result = av_scanner.has_virus(content, parallel=self.parallel)
        if av_result[0] is False:
            return super(AVFileSystemStorage, self).save(name, content, max_length)
        raise AVException(av_result[1])

class SingleCoreAVFileSystemStorage(AVFileSystemStorage):
    """
    Same as AVFileSystemStorage, but doesn't run multiple scanners in parallel
    """
    parallel = False
