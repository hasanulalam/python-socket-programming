import socket

BUFFSIZE = 1024
print "Starting client prog"
s = socket.socket()
host = 'cs3.kennesaw.edu'
port = 12321

'''
Variables for data manipulation.
arg_val =  Argument value for request type E.
request_type = Type of request to be sent.
poly = List of numbers.
a = value a for bisection.
b = value b for bisection.
tol = tolerance in bisection.
'''

request_type = 'E'
arg_val = 1.0
poly = [631,232,223,222]
a = 3
b = 2
tol = 0.00000000001

request = [request_type, arg_val,' ', poly]
#request = [request_type, a, ' ', b, ' ', poly, ' ', tol]
s.connect(('', port))
s.send(request)
recieve = s.recv(BUFFSIZE)
if (recieve[0] == 'E' || recieve[0] == 'S'):
    print(recieve)
else if(recive[0] == 'X')
    print(recieve)
s.close
