import numpy as np
import functools as ft
import itertools as it
import utils
from math import ceil

def inplace_rotate(image):
    assert(utils.equal(*image.shape)) #NxN
    N = image.shape[0] 
    #rotate 90degrees = change coordinatesystem (x,y)->(y,N-x)
    def rotate_pixel_quartet(image, x, y):
        """rotates a pixel quartet, i
        that is all 4pixels that needs to be moved
        (  x,  y),(  y,N-x),(N-x,N-y),(N-y,  x) //coordinate change 3 times
        """
        first_pixel = image[x,y]
        #copy backwards to save a few temporary variables
        image[    x,    y] = image[N-y-1,    x]
        image[N-y-1,    x] = image[N-x-1,N-y-1]
        image[N-x-1,N-y-1] = image[    y,N-x-1]
        image[    y,N-x-1] = first_pixel

    rotate = ft.partial(rotate_pixel_quartet, image)

#   now only do the quartet rotate on a chunk like this (else you will rotate the same pixel multiple time)
#
#   XXXX000
#   XXXX000
#   XXXX000
#   0000000
#   0000000
#   0000000
#   0000000
#
#   the box((0,0),(ceil(N/2.0),N//2)) show with 'X' works for both odd and even N
#   
#   added bonus: the center will not be copied at all if N is odd, and it is stationary

    list(it.starmap(
        rotate, 
        it.product(
            range(ceil(N/2.0)),
            range(N//2)
        )
    ))

eyes = [np.eye(N,dtype=int) for N in range(1,10)]

for eye in eyes:
    print("before:\n", eye)
    inplace_rotate(eye)
    print("after:\n", eye)

rndms = [ np.random.random_integers(0,9,size=(N,N)) for N in range(1,10) ]

for rndm in rndms: #the elements inside doesn't matter as long as they are unique
    print("before:\n", rndm)
    inplace_rotate(rndm)
    print("after:\n", rndm)
