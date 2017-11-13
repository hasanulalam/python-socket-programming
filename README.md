# SOCKET PROGRAMMING USING PYTHON

## Dependencies
I'm running a Mac OSX 10.3 running a Python 2.7. I've used inbuilt python modules `socket`,
`cPickle`, `time` and user defined module `polynomials`. Writing to a pascal file `save.pickle` and `response.pickle` for data transfer across
server and client.

## Modules
'cPickle' lets me send my data as a list over the connection. The two functions I've used from
that module are `cPickle.load()` and `cPickle.dump()` for sending and recieving data across the server.
cPickle uses a file to write to as a medium. I've used `save.p` and `response.p` for ensuring data
transfer.

`time` lets me pause the client to wait for server to process and write data to file to ensure data integrity.

## Algorithm
This program uses sockets to perform Client Server communication. It creates a socket and
uses Python inbuilt libraries `socket` and `cPickle` for sending data from server to client and
vice-versa.

## Scripts
`server.sh` to run server, `client.sh` to run client and `clear.sh` to clear data files.

###  NOTE
Each time the program is run, the client and server write to `save.p` and `response.p` for communication.
At the end of each run, the files must be cleared of data, to ensure smooth operation. I have written a
script `clear.sh` which clears the data files.
