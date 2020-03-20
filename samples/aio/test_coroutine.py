

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s' % n)
        r = '200 OK'

def produce(c):
    c.send(None)   #启动生成器，相当于next(c)
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCE] Producing %s' % n)
        r = c.send(n)
        print('[PRODUCE] Consumer return %s' % r)
    c.close()

if __name__ == '__main__':
    c = consumer()
    produce(c)

