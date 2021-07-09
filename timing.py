# took the idea from here and modified a bit
# https://codereview.stackexchange.com/questions/169870/decorator-to-measure-execution-time-of-a-function
from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print 'Elapsed time for {0}: {1}'.format(f.func_name, end-start)
        return result
    return wrapper
