import threading

local_school = threading.local()


def process_student():
    std = local_school.student
    tch = local_school.teacher
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))
    print('Hello, %s (in %s)' % (tch, threading.current_thread().name))


def process_thread(stu, tch):
    local_school.student = stu
    local_school.teacher = tch
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice', 'Mr Johnson'), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob', 'Ms Liu'), name='Thread-B')

t1.start()
t2.start()
t1.join()
t2.join()