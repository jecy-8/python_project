import os

print(dir(os.path))


def dir_l(Dir):
    print(Dir)
    for x in os.listdir(Dir):
        if os.path.isdir(x):
            nextDir = os.path.join(Dir, x)
            dir_l(nextDir)
        else:
            print(os.path.join(Dir, x))

def main():
    #dir_l(os.path.abspath('.'))
    dir_l(os.path.abspath('/Users/jecy/IdeaProjects/python_project'))

if __name__ == '__main__':
    main()


def dir_f1(Dir, KeyWord):
    for x in os.listdir(Dir):
        if os.path.isdir(x):
            nextDir = os.path.join(Dir, x)
            dir_l(nextDir, KeyWord)
        else:
            if x.find(KeyWord) != -1:
                print(os.path.join(Dir, x))

def main_f1(KeyWord):
    dir_f1(os.path.abspath('.'), KeyWord)

if __name__ == '__main__':
    main_f1('test')