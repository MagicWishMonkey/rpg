import sys
import traceback
from django.conf import settings
from .logger import log


class ErrorHandler(object):
    def process_exception(self, request, exception):
        type, value, tb = sys.exc_info()
        stack_trace = traceback.format_exception(type, value, tb)
        #print stack_trace

        message = exception.message
        message = "%s \n %s" % (message, stack_trace)#util.base64(stack_trace))
        print message

        try:
            log.exception(exception.message)
        except Exception:
            pass
        return None



def attach_values(request):
    """
    Return a template context for the current request, with application variables.
    """
    params = {
        'DEBUG': settings.DEBUG
    }
    return params