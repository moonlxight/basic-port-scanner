import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "" # Input IP here

for port in range(77, 65535):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        print("Port : " + str(port), " | Open")
    except Exception as e:
        print("Port : " + str(port), " | Closed")
        pass
    finally:
        pass
