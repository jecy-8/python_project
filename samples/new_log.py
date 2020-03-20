# -*- coding: utf-8 -*-
import functools,time


def new_log(arg):    # arg参数可代表自定义文本字符串，或function
    s = 'begin call'

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s: %s()' % (s, func.__name__))
            return_value = func(*args, **kw)
            print('end call: %s()' % func.__name__)
            return return_value
        return wrapper
    if isinstance(arg, str):  # arg 为自定义文本字符串
        s = arg  # 替换日志文本
        # 返回 decorator 函数，用于再次调用，传递 function 函数，返回 wrapper
        return decorator
    else:
        # 无自定义日志文本，arg 为 function 函数，调用 decorator 返回 wrapper
        return decorator(arg)


@new_log
def f1():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


@new_log('execute')
def f2():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

if __name__ == '__main__':
    f1()
    f2()