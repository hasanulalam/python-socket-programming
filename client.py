import Polynomials
import socket

BUFFSIZE = 1024
print "Starting client prog"
s = socket.socket()
host = 'cs3.kennesaw.edu'
#host = socket.gethostname()
port = 12321

s.connect((host, port))
print "Client connected to server: ", host
print "Sending my name to server ", host
s.send("Kshitij Bantupalli")
print s.recv(BUFFSIZE)
s.close
