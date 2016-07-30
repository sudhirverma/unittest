import os
import os.path


class RemovalService(object):

    def rm(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)
