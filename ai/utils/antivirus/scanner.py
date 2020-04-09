import os
import tempfile
from multiav.core import CMultiAV, AV_SPEED_MEDIUM


class AVScanner(object):
    def __init__(self):
        self.multi_av = CMultiAV("%s/cmultiav.cfg" % os.path.dirname(__file__))

    def has_virus(self, file, parallel=True):
        with tempfile.NamedTemporaryFile(delete=False) as temporaryfile:
            temporaryfile.write(file.read())
            temporaryfile.close()
            permission = 0o664  # PEP 3127: octal literals
            os.chmod(temporaryfile.name, permission)  # clamav needs permission to scan
            if parallel:
                # TODO: Handle the case for when no scanner is installed ...
                # Currently we say that nothing was found...
                # The single core case works as expected
                ret = self.multi_av.scan(temporaryfile.name, AV_SPEED_MEDIUM)
            else:

                try:
                    ret = self.multi_av.single_scan(temporaryfile.name, AV_SPEED_MEDIUM)
                except OSError:
                    # It would seem a scanner is not installed...
                    return True, "No virus scanner was found on the system..."

            os.unlink(temporaryfile.name)
            for x in list(ret.values()):
                if x != {}:
                    # all is lost as soon as one scanner finds something
                    return True, ret
            return False, None
