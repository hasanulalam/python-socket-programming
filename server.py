import pickle
import socket
import polynomials

BUFFSIZE = 1024
print "Starting server program."

#Create Sockets
try
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket successfully created."
except socket.error as err:
    print "Socket creation failed with error %s" %(err)

# Define the port to be used.
port = 12311
host = socket.gethostname()

'''
#Get IP of host.
try:
    host = socket.gethostname()
except socket.gaierror:
    print "There was an error resolving the host."          #Error control for host
    sys.exit()
'''

s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print 'Got connection from', addr
    #request = c.recv(BUFFSIZE)
    request = pickle.load(open("save.p", "rb"))
    if request[0] == 'E':
        if(len(request) < 4 or len(request) > 4):
            error = ['X', "Missing arguments."]
            #c.send(error)
            pickle.dump(error, open("save.p", "wb"))
            print("Shutting down server.")
            c.close()
        elif not(all(isinstance(item, int) for item in request[3])):
            error = ['X', "Invalid number format."]
            #c.send(error)
            pickle.dump(error, open("save.p", "wb"))
            print("Shutting down server.")
            c.close()
        else:
            x = request[1]
            poly = request[3]
            temp = polynomials.evaluate(x, poly)
            success = ['E', temp]
            #c.send(success)
            pickle.dump(success, open("save.p", "wb"))
            print ("Server finished. Shutting down.")
            c.close()
    elif request[0] == 'X':
        if(len(request) < 7 or len(request) > 7):
            error = ['X', "Missing Arguments"]
            #c.send(error)
            pickle.dump(error, open("save.p", "wb"))
            print("Shutting down server.")
            c.close()
        elif not(all(isinstance(item, int) for item in request[5])):
            error = ['X', "Invalid number format."]
            #c.send(error)
            pickle.dump(error, open("save.p", "wb"))
            print("Shutting down server.")
            c.close()
        else:
            a = request[1]
            b = request[3]
            poly = request[5]
            tol = request[7]
            temp = polynomials.bisection(a, b, poly, tol)
            success = ['S', temp]
            #c.send(success)
            pickle.dump(success, open("save.p","wb"))
            print("Server finished. Shutting down.")
            c.close()
    else:
        temp = "Please enter correct request type."
        error = ['X', temp]
        #c.send(error)
        pickle.dump(error, open("save.p", "wb"))
        print("Shutting down server.")
        c.close()
