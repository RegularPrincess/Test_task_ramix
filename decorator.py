# -*- coding: utf-8 -*-


import time


def measure_time(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print('%r затрачено %2.2f секунд' % \
              (method.__name__, te-ts))
        return result

    return timed


@measure_time
def fun1():
    print('fun3 start')
    time.sleep(1)
    return 'fun3 finish'


@measure_time
def fun2(a):
    print('fun3 start')
    print(a)
    time.sleep(2)
    return 'fun3 finish'


@measure_time
def fun3(a, *args, **kw):
    print('fun3 start')
    print(a)
    print(args)
    print(kw)
    time.sleep(0.3)
    return 'fun3 finish'

print(fun1(), '\n')
print(fun2(42), '\n')
print(fun3(42, 43, foo=2), '\n')
