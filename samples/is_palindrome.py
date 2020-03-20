# -*- coding: utf-8 -*-


def is_palindrome(n):

    def invert_str(s):
        list_str = s[-1]
        i = len(s) - 2
        while i >= 0:
            list_str += s[i]
            i -= 1
        return list_str

    n_str = str(n)
    size = len(n_str)

    if size == 1:
        return True
    left = n_str[:int(size / 2)]   #取前一半的序列
    right = n_str[-int(size / 2):]   #取后一半的序列

    if left == invert_str(right):
        return True
    return False


print(is_palindrome(2112))
print(is_palindrome(12321))
print(is_palindrome(1234))

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')






