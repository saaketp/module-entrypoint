import sys


def func():
    print(sys.argv)


sys.modules[__name__] = func
