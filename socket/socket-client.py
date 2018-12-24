'''
socket和http的区别：
http请求为单向，三次握手后，client可以向server发送数据，server接收，然后向client返回数据，client接收，连接close
而这个过程只能完成一次，server不能主动多次向client发送数据，需要频繁的三次握手连接
socket请求为双向，client和server都可以主动多次发送数据
'''
import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定IP和端口
client.connect(('localhost',8000))
client.send("boddy".encode("utf8"))
#client.close()