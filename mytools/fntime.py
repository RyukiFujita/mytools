import time
import colorful as cf
from functools import wraps

def fntime(fn) :
    @wraps(fn)
    def wrapper(*args, **kwargs) :
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        fn_name = cf.green(fn.__name__.ljust(30))
        proc_time = cf.yellow(f"{t2-t1:>15.10f}")
        print(f"function:{fn_name} took {proc_time} seconds")
        return result
    return wrapper
