import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 9999))
print(s.recv(1024).decode('utf-8'))

if __name__ == '__main__':
    for data in [b'Michael', b'Tracy', b'Sarah']:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    #发送结束消息
    s.send(b'exit')
    s.close()