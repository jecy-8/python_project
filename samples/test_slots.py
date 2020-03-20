
class Student(object):
    __slots__ = ('name', 'age', 'score')
    pass

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name


s = Student('Nancy')
s.age = '20'
s.score = 90

print(s)
print(s.name, s.age, s.score)
