#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def _private_1(name):
    print('Hello, %s' % name)


def _private_2(name):
    print('Hi, %s' % name)


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


greeting('Jecy')
greeting('Cat')
_private_2("hello")