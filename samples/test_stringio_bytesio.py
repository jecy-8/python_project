from io import StringIO
from io import BytesIO


# def outputstring():
#     return 'string \nfrom \noutputstring \nfunction'
#
#
# s = outputstring()
# sio = StringIO(unicode(s))
# print(sio.getvalue())
#
#
# s = sio.readlines()
# for i in s:
#     print(i.strip())
#
# sio = StringIO()
# sio.write(unicode(s))
# sio.seek(0, 0)
# print(sio.tell())
# s = sio.getvalue()
# print(s)
#
#
# bio = BytesIO()
# bio.write('This is for test bytes io'.encode('utf-8'))
# print(bio.getvalue())
# bio.seek(3, 1)
# print(bio.tell())
# print(bio.getvalue())
# for i in bio.readlines():
#     print(i.strip())
# bio.write('hhahh'.encode('utf-8'))
# print(bio.getvalue())

x = file('/Users/jecy/IdeaProjects/python_project/samples/hello.py', 'r')
print(x.tell())

#默认从文件开始位置
x.seek(3)
print(x.tell())

x.seek(5)
print(x.tell())

#从文件当前位置
x.seek(2, 1)
print(x.tell())

#从文件结束位置
x.seek(2, 2)
print(x.tell())

x.seek(0, 2)
print(x.tell())

x.seek(-3, 2)
print(x.tell())

