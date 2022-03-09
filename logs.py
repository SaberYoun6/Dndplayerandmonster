import logging
import os
import settings

class Logger(object):

    def__init__(self,name):
        name = name.replace('.log','')
        logger - logging.getLogger('log_namespace.%s' %name)
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            file_name = os.path.join(settings.LOGGING_DIR, '%s.log' % name)
            formatter = logging.Formatter('%(asctime)s %(levelname)s:%(name)s %(message)s')
            handler.setFormatter(formatter)
            handler.setLevel(logging.DEBUG)
            logger.addHandler(handler)
        self._logger = logger

    def get(self):
        return._logger

