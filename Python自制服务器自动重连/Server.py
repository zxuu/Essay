import socket
import threading
import json

class Server(object):
    def __init__(self, host, port):
        self.host = host #ip地址
        self.port = port #端口号
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #创建一个套接字，采用tcp连接
        #设置socket，第一个参数使用正在使用的socket选项，第二个参数代表当socket关闭后，本地端用
        # 于该socket的端口号立刻就可以被重用。通常来说，只有经过系统定义一段时间后，才能被重用。
        #1表示将SO_REUSEADDR标记为TRUE
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port)) #将端口号绑定到IP地址

    def listen(self):
        self.sock.listen(1)
        while True:
            client, address = self.sock.accept() #接受客户端的连接请求
            client.settimeout(60) #如果重连60秒后还没有连上则断开连接
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024 #一次接收最大字节数
        while True:
            try:
                data = client.recv(size)
                datastr = data.decode() #解码为字符串
                if datastr == "3":
                    print(datastr)
                    sendData = {
                        '1': 3,
                        '2': "桌子",
                        '3': "椅子"
                    }
                    messagestr = json.dumps(sendData)
                    message = bytes(messagestr, encoding="utf8") #将字符串转换为字节流
                    client.send(message) #发送字节流
                elif datastr == "4":
                    print(datastr)
                    sendData = {
                        '1': 4,
                        '2': "眼镜"
                    }
                    messagestr = json.dumps(sendData)
                    message = bytes(messagestr, encoding="utf8")
                    client.send(message)
                elif datastr == "5":
                    print(datastr)
                    sendData = {
                        '1': 5,
                        '2': "眼镜"
                    }
                    messagestr = json.dumps(sendData)
                    message = bytes(messagestr, encoding="utf8")
                    client.send(message)
                else:
                    # raise socket.error('Client disconnected')
                    pass
            except:
                # client.close()
                # return False
                pass

def getip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("www.baidu.com", 0))
        ip = s.getsockname()[0]
        print(ip)
    except:
        ip = "x.x.x.x"
    finally:
        s.close()
    return ip
if __name__ == "__main__":
    while True:
        port_num = 7653 #约定的端口号
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass
    Server(getip(),port_num).listen()