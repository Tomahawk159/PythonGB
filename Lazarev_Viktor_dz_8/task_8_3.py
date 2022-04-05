from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for element in args:
            print(f'{func.__name__} ({element} : {type(element)})')
            func(*args)
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


calc_cube(5)
