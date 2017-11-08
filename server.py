import socket

BUFFSIZE = 1024
print "Starting server prog"
s = socket.socket()
#host = socket.gethostname()
port = 12321
s.bind(('', port))

s.listen(5)
while True:
    c, addr = s.accept()
    print 'Got connection from', addr
    namedata = c.recv(BUFFSIZE)
    print 'recieved: ', namedata
    c.send(host + 'Ending connection to: ')
    c.close()
