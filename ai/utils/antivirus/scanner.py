# -*- coding: utf-8 -*-
import os
import tempfile
from multiav.core import CMultiAV, AV_SPEED_MEDIUM


class AVScanner(object):
    def __init__(self):
        self.multi_av = CMultiAV("%s/cmultiav.cfg" % os.path.dirname(__file__))

    def has_virus(self, file):
        with tempfile.NamedTemporaryFile(delete=False) as temporaryfile:
            temporaryfile.write(file.read())
            temporaryfile.close()
            ret = self.multi_av.scan(temporaryfile.name, AV_SPEED_MEDIUM)
            os.unlink(temporaryfile.name)
            if ret != {}:
                return True, ret
            return False, None
