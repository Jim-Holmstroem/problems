
import numpy as np

def zeroout(matrix):
    zero_cols, zero_rows = (np.all(matrix, axis=i) for i in [0,1])
    for row in np.where(zero_rows==0):
        matrix[row,:] = 0
    for col in np.where(zero_cols==0):
        matrix[:,col] = 0


rndms = [ np.random.random_integers(0,20,size=(N,N+2)) for N in range(1,10) ]

for rndm in rndms: #the elements inside doesn't matter as long as they are unique
    print("before:\n", (rndm!=0).astype(int)) #only a view of the nonzero elements
    zeroout(rndm)
    print("after:\n", (rndm!=0).astype(int))
