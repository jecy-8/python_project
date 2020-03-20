# class Hello(object):
#     def hello(self, name='world'):
#         print('Hello %s' % name)
#
#
# h = Hello()
# h.hello()
# h.hello('Test')
#
#
# def fn(self, name='Test'):
#     print('Hi %s' % name)
#
#
# Hi = type('Hi', (object,), dict(hi=fn))
#
# h1 = Hi()
# h1.hi()


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


l = MyList()
l.add(1)
print(l)

'''
gjeoage jgieowg
'''
