'''
# Kshitij Bantupalli
# CS6025 : Assignment 6
#
#   SERVER SIDE
#
# Dependencies : I'm running a Mac OSX 10.3 running a Python 2.7. I've used inbuilt python modules socket and pickle and user defined module polynomials.
# Writing to a pascal file "save.p" for data transfer across server and client.
#
# Algorithm : This program uses sockets to perform Client Server communication. It creates a socket and uses Python inbuilt libraries 'socket' and 'pickle' for sending data
# from server to client and vice-versa.
#
# 'pickle' lets me send my data as a list over the connection. The two functions I've used from that module are pickle.load() and pickle.dump() for sending and recieving data across the server.
# pickle uses a file to write to as a medium. I've used "save.p" for ensuring data transfer.
#
############################################################################################ NOTE ###############################################################################################
#   Each time the program is run, the file "save.p" has to be either (a) Deleted and replaced by a new "save.p" or (b) Deleted of all content. Please ensure this, or its gonna run into an error.
#
#
'''

#########################
#####  MODULES ##########
#########################
import pickle
import socket
import polynomials

BUFFSIZE = 1024
print "Starting server program."

# Define the port to be used.
port = 12311
host = socket.gethostname()

#Create Sockets
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket successfully created."
except socket.error as err:
    print "Socket creation failed with error %s" %(err)

s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print 'Got connection from', addr
    request = pickle.load(open("save.p", "rb"))                                 #Recieving the request from the client.
    if request[0] == 'E':
        '''
        Error checking for request type 'E'. I've tested for missing arguments and non integer Polynomials.
        '''
        if(len(request) < 4 or len(request) > 4):
            error = ['X', "Missing arguments."]
            pickle.dump(error, open("save.p", "wb"))
            print("Shutting down server.")
            c.close()
        elif not(all(isinstance(item, int) for item in request[3])):
            error = ['X', "Invalid number format."]
            pickle.dump(error, open("save.p", "wb"))
            print("Shutting down server.")
            c.close()
        '''
            Error checking ends.
        '''
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
        '''
        Error checking for request type 'X'. I've tested for missing arguments and non integer polynomials.
        '''
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
        '''
            Error checking ends.
        '''
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
        '''
            Error checking for wrong request type.
        '''
        temp = "Please enter correct request type."
        error = ['X', temp]
        #c.send(error)
        pickle.dump(error, open("save.p", "wb"))
        print("Shutting down server.")
        c.close()
