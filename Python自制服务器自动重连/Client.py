import os,sys,time
import socket

def doConnect(host,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try :
        sock.connect((host,port))
    except :
        pass
    return sock

def main():
    host,port = "192.168.43.6",7653
    print(host,port)
    sockLocal = doConnect(host,port)

    while True :
        try :
            msg = str(time.time())
            message = bytes(msg, encoding="utf8")
            sockLocal.send(message)
            print("send msg ok : ",message)
            print("recv data :",sockLocal.recv(1024))
        except socket.error :
            print("\r\nsocket error,do reconnect ")
            time.sleep(3)
            sockLocal = doConnect(host,port)
        except :
            print('\r\nother error occur ')
            time.sleep(3)
        time.sleep(1)

if __name__ == "__main__" :
    main()