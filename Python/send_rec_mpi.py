#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:     
# Purpose:  
# Version:      1.0
# Licence:      MIT Licence
# Author:       Jack Simpson
# Email:        jack@jacksimpson.co
# Created:      2015-10-27
#-------------------------------------------------------------------------------
# These modules are available in the Standard Library of Python

# These modules come from third party libraries
from mpi4py import MPI

def main():
    comm = MPI.COMM_WORLD
    rank = comm.rank # id of node
    size = comm.size # how many nodes are in the system
    name = MPI.Get_processor_name() # name of the processor (hostname)
    
    shared = rank + 5 # could also send a dictionary, list, etc
    
    if rank == 0:
        data = shared
        comm.send(data, dest=1, tag=1) # tag ensures order that messages are sent and received in
        print ('From rank' rank, 'we sent', data)

    elif rank == 1:
        data = comm.recv(source=0, tag=1)
         print ('On rank' rank, 'we received:', data)

if __name__ == "__main__":
    main()
        
