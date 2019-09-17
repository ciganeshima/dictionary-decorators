import time
from inspect import isfunction, isclass


def profile(f):
    if isfunction(f):
        def wrapper(*args, **kwargs):
            start_time = time.clock()
            if isfunction(f):
                print("'{}' started".format(f.__qualname__))
                k = f(*args, **kwargs)
                print("'{}' finished in {}".format(f.__qualname__, time.clock() - start_time))
            return(k)
        return wrapper

    if isclass(f):
        klass=f
        for attr_name in klass.__dict__.items():
            if isfunction(attr_name[1]):
                attr = getattr(klass, attr_name[0])
                setattr(klass, attr_name[0], profile(attr))
        return klass


@profile
class MyClass:
    def __init__(self):
        pass
    def decorating_method(self):
        print('Hello from the decorating method')
    def rofl(self):
        print('Hello from the rofl method')


@profile
def test():
    print("Hello from function")

MyClass()
test()

