import time
import pandas as pd
def log(path):
    def decorator(function):
        def wraper(*arg, **kwargs):
            t1 = time.ctime(time.time())
            return_value = function(*arg, **kwargs)
            t2 = time.ctime(time.time())
            df = pd.DataFrame({'time': [t1, t2], 'return': return_value, 'arg': arg})
            df.to_csv(path, sep = ' ', index = False)
            return return_value
        return wraper
    return decorator
@log('log.txt')
def summ(a, b):
    return a + b
s = summ(1, 2)
