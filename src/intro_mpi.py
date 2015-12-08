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

    print ('Hi, my name is', name, 'my rank is:', rank, 'size of cluster:', size)
   
    if rank == 0:
        print ('Working on the task for rank', rank)

    if rank == 1:
        print ('Working on the task for rank', rank)
    
    if rank == 3:
        print ('Working on the task for rank', rank)


if __name__ == "__main__":
    main()
        
