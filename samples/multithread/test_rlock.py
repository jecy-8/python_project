import threading, time

g_num = 0
r_lock = threading.RLock()

def func():
    global  g_num
    r_lock.acquire()
    g_num += 1
    time.sleep(1)
    print(g_num)
    r_lock.release()

if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=func)
        t.start()