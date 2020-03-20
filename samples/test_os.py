import os

print(os.name)
print(os.uname())
print(os.environ)
print(os.environ.get('PATH'))
print(os.path.abspath('.'))
print(os.path.join(os.path.abspath('.'), 'test'))
os.mkdir('/Users/jecy/IdeaProjects/python_project/samples/test1')
print(os.listdir('.'))
os.rmdir('/Users/jecy/IdeaProjects/python_project/samples/test1')
print(os.listdir('.'))
print(os.path.split('Users/jecy/IdeaProjects/python_project/samples/hello.py'))
print(os.path.splitext('Users/jecy/IdeaProjects/python_project/samples/hello.py'))

print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.txt'])
