import Polynomials
import socket

BUFFSIZE = 1024
print "Starting server program."

#Create Sockets
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket successfully created."
except socket.error as err:
    print "Socket creation failed with error %s" %(err)

# Define the port to be used.
port = 12321

'''
#Get IP of host.
try:
    host = socket.gethostname('cs3.kennesaw.edu')
except socket.gaierror:
    print "There was an error resolving the host."          #Error control for host
    sys.exit()
'''

s.bind(('', port))

s.listen(5)
while True:
    c, addr = s.accept()
    print 'Got connection from', addr
    request = c.recv(BUFFSIZE)
    if request[0] = 'E':
        if(len(request) < 4 || len(request) > 4):
            error = ['X', "Missing arguments."]
            c.send(error)
            print("Shutting down server.")
            c.close()
        else if !(all(isinstance(item, int) for item in request[4])):
            error = ['X', "Invalid number format."]
            c.send(error)
            print("Shutting down server.")
            c.close()
        else:
            x = request[1]
            poly = request[4]
            temp = evaluate(x, poly)
            success = ['E', temp]
            c.send(success)
            print ("Server finished. Shutting down.")
            c.close()
    else if request[0] = 'X':
        if(len(request) < 7 || len(request) > 7):
            error = ['X', "Missing Arguments"]
            c.send(error)
            print("Shutting down server.")
            c.close()
        else if !(all(isinstance(item, int) for item in request[5])):
            error = ['X', "Invalid number format."]
            c.send(error)
            print("Shutting down server.")
            c.close()
        else:
            a = request[1]
            b = request[3]
            poly = request[5]
            tol = request[7]
            temp = bisection(a, b, poly, tol)
            success = ['S', temp]
            c.send(success)
            print("Server finished. Shutting down.")
            c.close()
    else:
        temp = "Please enter correct request type."
        error = ['X', temp]
        c.send(error)
        print("Shutting down server.")
        c.close()