from functools import wraps


def val_checker(arg_decor):
    def decorator(func):
        @wraps(func)
        def wrapper(num):
            if arg_decor(num):
                result = func(num)
                return result
            else:
                raise ValueError(f'wrong val {num}')
        return wrapper
    return decorator


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


results = calc_cube(5)
print(results)
