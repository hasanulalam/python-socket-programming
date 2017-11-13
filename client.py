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
import cPickle as pickle
import time

BUFFSIZE = 1024
print "Starting client prog"

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket successfully created."
except socket.error as err:
    print "Socket creation failed with error %s" %(err)

host = ''
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

request_type = 'S'
arg_val = 1
poly = [-945, 1689, -950, 230, -25, 1]
a = 0
b = 2
tol = 0.0000000000000015

'''
ENSURE CORRECT REQUEST TYPE
'''
#request = [request_type, arg_val,' ', poly]
request = [request_type, a, ' ', b, ' ', poly, ' ', tol]
s.connect((host, port))


with open ("save.p", 'wb') as o:
    pickle.dump(request, o)

'''
PUTTING THE CLIENT PROGRAM TO SLEEP TO ENSURE, SERVER HAS TIME TO WRITE TO THE FILE.
'''
time.sleep(2)

with open("response.p", 'rb') as o:
    recieve = pickle.load(o)



if (recieve[0] == 'E' or recieve[0] == 'S'):
    print ''.join(map(str, recieve))
elif (recieve[0] == 'X'):
    print ''.join(map(str, recieve))
s.close
