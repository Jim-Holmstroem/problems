from utils import bitcount

def bitdiff(a, b):
    return bitcount(a^b) #count the bits that differs

