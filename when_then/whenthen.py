def whenthen(func):
    list_when = []
    list_then = []

    def new_func(*args, **kwargs):
        if len(list_when) == len(list_then):
            for when, then in zip(list_when, list_then):
                if when(*args, **kwargs):
                    return then(*args, **kwargs)
        else:
            raise ValueError
        return func(*args, **kwargs)

    def when(f):
        if len(list_when) == len(list_then):
            list_when.append(f)
        else:
            raise ValueError
        return new_func

    def then(f):
        if len(list_when) == len(list_then) + 1:
            list_then.append(f)
        else:
            raise ValueError
        return new_func

    new_func.when = when
    new_func.then = then

    return new_func


@whenthen
def fract(x):
    return x * fract(x - 1)


@fract.when
def fract(x):
    return x == 0


@fract.then
def fract(x):
    return 1


@fract.when
def fract(x):
    return x > 5


@fract.then
def fract(x):
    return x * (x - 1) * (x - 2) * (x - 3) * (x - 4) * fract(x - 5)


@fract.when
def fract(x):
    return x < 0


@fract.then
def fract(x):
    return 'nevozmojno'

print(fract(0))
print(fract(1))
print(fract(6))
print(fract(-1))