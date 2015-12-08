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
    
    if rank == 0:
        data = [num for num in range(size)]
        print('Data to scatter', data)
    else:
        data = None

    data = comm.scatter(data, root=0):
    print ('rank', rank, data)

    all_data = comm.gather(data, root=0)

    if rank == 0:
        print ('Master collected', all_data) # get back original list

if __name__ == "__main__":
    main()
        
