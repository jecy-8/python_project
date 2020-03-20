import threading, time


num = 0
semaphore = threading.BoundedSemaphore(5)

def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("Run thread %s\n" % n)
    semaphore.release()


if __name__ == '__main__':
    for i in range(20):
        t = threading.Thread(target=run, args=('t-%s' % i,))
        t.start()

    while threading.active_count() != 1:
        pass #print('thread active count: %s' % threading.active_count())
    else:
        print('-------all threads done------')