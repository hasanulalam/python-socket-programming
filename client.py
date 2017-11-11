'''
#
# Kshitij Bantupalli
# CS 6025 : Assignment 6
#
#   CLIENT SIDE
#
#
'''
import socket
import pickle

BUFFSIZE = 1024
print "Starting client prog"

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket successfully created."
except socket.error as err:
    print "Socket creation failed with error %s" %(err)

host = 'cs3.kennesaw.edu'
port = 12311



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

#request = [request_type, arg_val,' ', poly]
request = [request_type, a, ' ', b, ' ', poly, ' ', tol]
s.connect((host, port))

with open('request.pickle', 'wb') as f:
    pickle.dump(request, f, pickle.HIGHEST_PROTOCOL)

with open('response.pickle', 'rb') as g:
    recieve = pickle.load(g)
    
if (recieve[0] == 'E' or recieve[0] == 'S'):
    print ''.join(map(str, data))
elif (recieve[0] == 'X'):
    print ''.join(map(str, data))
s.close
