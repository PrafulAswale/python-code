import time


def timer(fx):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fx(*args, **kwargs)
        end = time.time()
        print(f"{fx.__name__} ran in {end-start} time")
        return result
    return wrapper


@timer
def example_function(n):
    time.sleep(n)


example_function(2)
