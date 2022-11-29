import socket

HOST = '140.116.118.130'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

print('Server start at: %s:%s' % (HOST, PORT))
print('Waiting for connection...')

while True:
	conn, addr = s.accept()
	print('Connected by ' + str(addr))
	
	while True:
		indata = conn.recv(1024)
		if indata.decode() == "EXIT": #connection closed
			conn.close()
			print(str(addr)+'closed connection.')
			break
        	
		print(str(addr) + ": " + indata.decode())
		outdata = indata.decode()
		conn.send(outdata.encode())
	