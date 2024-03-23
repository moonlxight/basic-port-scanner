import socket

ip = "" # Input IP here

for port in range(1, 100):

	try:

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		s.settimeout(20.0)

		s.connect((ip, port))

		response = s.recv(1024)



		print(str(port),": open : Banner : ", response.decode())

	except Exception as e:

		print(str(port), ": closed : Reason :", str(e))

		pass

	finally:

		s.close()