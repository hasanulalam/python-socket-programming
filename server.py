'''
# Kshitij Bantupalli
# CS6025 : Assignment 6
#
#   SERVER SIDE
#
# Dependencies : I'm running a Mac OSX 10.3 running a Python 2.7. I've used inbuilt python modules socket and
# cPickle and user defined module polynomials. Writing to a pascal file "save.pickle" for data transfer across
# server and client.
#
# Modules : 'cPickle' lets me send my data as a list over the connection. The two functions I've used from
# that module are cPickle.load() and cPickle.dump() for sending and recieving data across the server.
# cPickle uses a file to write to as a medium. I've used "save.p" and "response.p" for ensuring data
# transfer.
#
# 'time' lets me pause the client to wait for server to process and write data to file to ensure data integrity.
#
# Algorithm : This program uses sockets to perform Client Server communication. It creates a socket and
# uses Python inbuilt libraries 'socket' and 'cPickle' for sending data from server to client and
# vice-versa.
#
# Scripts : "server.sh" to run server, "client.sh" to run client and "clear.sh" to clear data files.
#
###############################      NOTE     ######################################
# Each time the program is run, the client and server write to "save.p" and "response.p" for communication.
# At the end of each run, the files must be cleared of data, to ensure smooth operation. I have written a
# script "clear.sh" which clears the data files.
'''

#########################
#####  MODULES ##########
#########################
import cPickle as pickle
import socket
import polynomials


def err (e):
        with open("response.p", 'wb') as o:
            pickle.dump(e, o)



def eval (e):
        with open("response.p", 'wb') as o:
            pickle.dump(e, o)


def bisec (e):
        with open("response.p", 'wb') as o:
            pickle.dump(e, o)



BUFFSIZE = 1024
print "Starting server program."

# Define the port to be used.
port = 12321
#host = socket.gethostname()

#Create Sockets
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket successfully created."
except socket.error as err:
    print "Socket creation failed with error %s" %(err)

s.bind(('', port))

s.listen(5)
while True:
    c, addr = s.accept()
    print 'Got connection from', addr
    with open("save.p", 'rb') as f:
        request = pickle.load(f)

    if request[0] == 'E':
        '''
        Error checking for request type 'E'.
        I've tested for missing arguments
        and non integer Polynomials.
        '''
        if(len(request) < 4 or len(request) > 4):
            error = ['X', "Missing arguments."]
            err(error)
            print("Shutting down server.")
            c.close()
        elif not(all(isinstance(item, int) for item in request[3])):
            error = ['X', "Invalid number format."]
            err(error)
            print("Shutting down server.")
            c.close()
        else:
            x = request[1]
            poly = request[3]
            temp = polynomials.evaluate(x, poly)
            success = ['E', temp]
            #c.send(success)
            eval(success)
            print ("Server finished. Shutting down.")
            c.close()
    elif request[0] == 'S':
        '''
        Error checking for request type 'X'.
        I've tested for missing arguments
        and non integer polynomials.
        '''
        if(len(request) < 8 or len(request) > 8):
            error = ['X', "Missing Arguments"]
            #c.send(error)
            err(error)
            print("Shutting down server.")
            c.close()
        elif not(all(isinstance(item, int) for item in request[5])):
            error = ['X', "Invalid number format."]
            #c.send(error)
            err(error)
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
            bisec(success)
            print("Server finished. Shutting down.")
            c.close()
    else:
        '''
            Error checking for wrong request type.
        '''
        temp = "Please enter correct request type."
        error = ['X', temp]
        #c.send(error)
        err(error)
        print("Shutting down server.")
        c.close()
