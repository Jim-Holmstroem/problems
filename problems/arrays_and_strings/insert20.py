
import utils
import itertools as it

def simple_insert20(string):
    """will not handle multiple inner spaces with multiple %20, 
    but is both simple and fast"""
    return '%20'.join(string.split())

def inplace_insert20(string):
    """ assuming we have extra space so it always fits into already allocated
    it acts a little bit weird if there are more trailing spaces then needed
    """
    def is_space(t):
        return t == 32
    assert(isinstance(string, bytearray)) #bytearray(b'example')
    
    inserted = b'%20'
    len_inserted = len(inserted)
    len_string = len(string)
    i=0
    while i<len_string: #a little bit ugly, should do this recursivly
        if(is_space(string[i])):
            if(i+len_inserted<len_string):
                string[i+len_inserted:] = string[i+1:1-len_inserted] #think that these are inplace
                string[i:i+len_inserted] = inserted
            i+=len_inserted
        else:
            i+=1

#test = bytearray(b' ad ad  ad          ')
#inplace_insert20(test)
#print(test)
