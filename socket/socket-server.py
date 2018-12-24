import socket

'''
AF_INET为IPV4，AF_INET6为IPV6，AF_IPX为linux下进程监听服务
SOCK_STREAM为TCP，SOCK_DGRAM为UDP
指明socket网络类型为IPV4，协议为TCP
也可直接用server = socket.socket()
'''
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定IP和端口
server.bind(('0.0.0.0',8000))
#开启监听
server.listen()
finished = False
#循环监听8000端口等待客户端的连接请求

while True:

    #接受客户端的连接请求，并为其创建套接字sock
    sock, addr = server.accept()
    #获取从客户端发送的数据
    #一次获取1K的数据
    while not finished:
        data = sock.recv(1024)
        if data.decode('utf8') != 'exit':
            print('client:{}'.format(data.decode("utf8")))
            msg = input('server:')
            sock.send(msg.encode('utf8'))
        else:
            sock.close()
            finished = True
# socket.close()
