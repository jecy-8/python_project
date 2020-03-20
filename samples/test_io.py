# try:
#     f = open('/Users/jecy/IdeaProjects/python_project/samples/hello.py', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()


# with open('/Users/jecy/IdeaProjects/python_project/samples/hello.py', 'r') as f:
#     for line in f.readlines():
#         print(line.strip())


# with open('/Users/jecy/IdeaProjects/python_project/samples/hello.py', 'rb') as f:
#     for line in f.readlines():
#         print(line.strip())


f = open('/Users/jecy/IdeaProjects/python_project/samples/test.txt', 'a')
f.write('\nThis is for testing1')
f.close()