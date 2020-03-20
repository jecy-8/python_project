import hashlib


def calc_md5(filename):
    icon = open(filename, 'rb')
    icon_content = icon.read()
    icon.close()
    return hashlib.md5(icon_content).hexdigest()



if __name__ == '__main__':
    print(calc_md5('question.png'))