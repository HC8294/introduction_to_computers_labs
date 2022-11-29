import socket
import threading

def client(i):
  while Ture:
    conni=conn
    addri=addr
    indata=conni.recv(1024)
    if indata.decode() == "EXIT":
      conni.close()
      print(str(addri)+'closed connection.')
      print("Wait for connection.")
      break
    else:
      print(str(addri) + ": " + indata.decode())
      print(str(addri) + ": " + indata.decode())
      conn.send(outdata.encode())

HOST = '140.116.118.130'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

print('Server start at: %s:%s' % (HOST, PORT))
print('Waiting for connection...')

threads = []
i=0

while True:
	conn, addr = s.accept()
	print('Connected by ' + str(addr))
	threads.append(threading.Thread(target = client, args = (i,)))
	threads[i].start()
	i+=1