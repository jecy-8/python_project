import socket

#创建一个socket，SOCK_DGRAM指定这个Socket类型是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#绑定端口, UDP不需要调用listen()
#服务器绑定UDP端口和TCP端口互不冲突，也就是说，UDP的9999端口与TCP的9999端口可以各自绑定
s.bind(('127.0.0.1', 9999))


if __name__ == '__main__':
    print('Bind UDP on 9999...')
    while True:
        #接收数据
        data, addr = s.recvfrom(1024)
        print('Received from %s:%s.' % addr)
        if not data or data.decode('utf-8') == 'exit':
            break
        s.sendto(b'Hello %s!' % data, addr)
    s.close()

