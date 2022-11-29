import socket

HOST = '140.116.118.130'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Connected to: %s:%s' % (HOST, PORT))

while True:
    outdata = input('Send: ')
    s.send(outdata.encode())
    
    indata = s.recv(1024)
    if len(indata) == 0: # connection closed
        s.close()
        print('Closed connection.')
        break
    print('Echo: ' + indata.decode())