import socket

'''
AF_INET为IPV4，AF_INET6为IPV6，AF_IPX为linux下进程监听服务
SOCK_STREAM为TCP，SOCK_DGRAM为UDP
指明socket网络类型为IPV4，协议为TCP
'''
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定IP和端口
server.bind(('0.0.0.0',8000))
#开启监听
server.listen()
#接收服务器的返回
sock, addr = server.accept()
