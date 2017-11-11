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
    with open('request.pickle', 'rb') as f:
        request = pickle.load(f)                                 #Recieving the request from the client.
    if request[0] == 'E':
        '''
        Error checking for request type 'E'. I've tested for missing arguments and non integer Polynomials.
        '''
        if(len(request) < 4 or len(request) > 4):
            response = ['X', "Missing arguments."]
            with open('response.pickle', 'wb') as f:
                pickle.dump(response, f, pickle.HIGHEST_PROTOCOL)
            print("Shutting down server.")
            c.close()
        elif not(all(isinstance(item, int) for item in request[3])):
            response = ['X', "Invalid number format."]
            with open('response.pickle', 'wb') as f:
                    pickle.dump(reponse, f, pickle.HIGHEST_PROTOCOL)
            pickle.dump(error, open("save.p", "wb"))
            print("Shutting down server.")
            c.close()
        else:
            x = request[1]
            poly = request[3]
            temp = polynomials.evaluate(x, poly)
            response = ['E', temp]
            with open('response.pickle', 'wb') as f:
                pickle.dump(response, f, pickle.HIGHEST_PROTOCOL)
            print ("Server finished. Shutting down.")
            c.close()
    elif request[0] == 'X':
        '''
        Error checking for request type 'X'. I've tested for missing arguments and non integer polynomials.
        '''
        if(len(request) < 7 or len(request) > 7):
            response = ['X', "Missing Arguments"]
            with open('response.pickle', 'wb') as f:
                pickle.dump(response, f, pickle.HIGHEST_PROTOCOL)
            print("Shutting down server.")
            c.close()
        elif not(all(isinstance(item, int) for item in request[5])):
            response = ['X', "Invalid number format."]
            with open('response.pickle', 'wb') as f:
                pickle.load(response, f, pickle.HIGHEST_PROTOCOL)
            print("Shutting down server.")
            c.close()
        else:
            a = request[1]
            b = request[3]
            poly = request[5]
            tol = request[7]
            temp = polynomials.bisection(a, b, poly, tol)
            response = ['S', temp]
            with open('response.pickle', 'wb') as f:
                pickle.load(response, f, pickle.HIGHEST_PROTOCOL)
            print("Server finished. Shutting down.")
            c.close()
    else:
        '''
            Error checking for wrong request type.
        '''
        temp = "Please enter correct request type."
        response = ['X', temp]
        with open('response.pickle', 'wb') as f:
            pickle.load(response, f, pickle.HIGHEST_PROTOCOL)
        print("Shutting down server.")
        c.close()
