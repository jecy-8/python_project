#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        else:
            return 'C'

if __name__ == '__main__':
    student_a = Student('Lucy', 20, 85)
    student_a.print_score()
    print(student_a.get_grade())
