#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# def outer_func():
#     loc_list = []
#
#     def inner_func(name):
#         loc_list.append(len(loc_list) + 1)
#         print('%s loc_list = %s' % (name, loc_list))
#     return inner_func
#
#
# clo_func_0 = outer_func()
# clo_func_0('clo_func_0')
# clo_func_0('clo_func_0')
# clo_func_0('clo_func_0')
#
# clo_func_1 = outer_func()
# clo_func_1('clo_func_1')
# clo_func_0('clo_func_0')
# clo_func_1('clo_func_1')


def my_func(*args):
    fs = []
    for i in range(3):
        def func(_i = i):
            return _i * _i
        fs.append(func)
    return fs


fs1,fs2,fs3 = my_func()
print(fs1())
print(fs2())
print(fs3())