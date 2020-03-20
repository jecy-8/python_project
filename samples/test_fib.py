class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

    def __getattr__(self, attr):
        if attr == 'name':
            return "Michael"
        if attr == 'age':
            return lambda: 25
        raise AttributeError('No such attribute: %s' % attr)

    def __call__(self):
        print('Hello %s' % self.name)


fib = Fib()
for i in fib:
    print(i)

print(fib[5])
print(fib[0:5])
print(fib.name)
print(fib.age)
# print(fib.score)
fib()

