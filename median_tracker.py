from __future__ import print_function
import heapq as h
import utils
import collections  as c
import operator as op
import random as rndm
import itertools as it


class median_tracker(object):
    """
    tracks medians of the appended numbers
    by having ``equally'' sized min- and maxheap pair.
    [max_heap] + [min_heap] and to get median we access need (at most)
    access the biggest element in max_heap and smallest element in min_heap

    min_heap = contains the bigger half
    max_heap = contains the smaller half

    median = O(1)
    append = O(log(n))
    """
    def __init__(self, *elems):
        self.min_heap = []
        self.max_heap = [] #will only contain negations of the numbers put in to it, easiest way todo max heap in python
        self.append(*elems)

    def push_min(self, elem):
        h.heappush(self.min_heap, elem)
    def push_max(self, elem):
        h.heappush(self.max_heap, -elem)
    def pop_min(self):
        return h.heappop(self.min_heap)
    def pop_max(self):
        return h.heappop(self.max_heap)
    def len_min(self):
        return len(self.min_heap)
    def len_max(self):
        return len(self.max_heap)
    def get_min(self): #NOTE will only return the smallest element in the biggest half
        return self.min_heap[0]
    def get_max(self): #NOTE will only return the biggest element in the smallest half
        return -self.max_heap[0]

    def append(self, *elems):
        map(self.append_elem, elems)
    def append_elem(self, elem):
        #start cases
        if(self.len_min()==0 and self.len_max()==0):
            self.push_max(elem)
            return

        #decide where to put it
        if(elem<=self.get_max()): #fits in the smallest half
            self.push_max(elem)
        elif(self.len_min>0 or elem>=self.get_min()): #fits in the biggest half
            self.push_min(elem)
        else:
            raise Exception()

        #rebalance the heaps #NOTE can only be unbalanced by one 
        if(abs(self.len_max()-self.len_min())>1): #unbalanced, let's go ``robin hood''
            if(self.len_min()<self.len_max()):
                self.push_min(self.pop_max()) 
            elif(self.len_max()<self.len_min()):
                self.push_max(self.pop_min()) 
            else:
                raise Exception()


    def __str__(self):
        """shows both heaps flatted out with each others roots touching"""
        return "{max_heap_reversed}|{min_heap}".format(
            max_heap_reversed=map(
                op.neg,
                reversed(self.max_heap)
            ), 
            min_heap=self.min_heap
        )

    def median(self):
        """O(1)"""
        if( self.len_min()+self.len_max()==0 ): #has elements at all
            raise Exception()
        elif( self.len_min()==self.len_max() ):
            return float(self.get_max()+self.get_min())/2 
        elif( self.len_min()<self.len_max() ):
            return float(self.get_max()) 
        elif( self.len_max()<self.len_min() ):
            return float(self.get_min())
        else:
            raise Exception()


ref_median = utils.median

test_list = [1,2,3,4,5,6,7,8]
mt = median_tracker(*test_list)

def random_list(size, domain=(-2,2)):
    return (rndm.uniform(domain[0], domain[1]) for i in range(size))

tests = map(
    random_list,
    it.chain.from_iterable(
        map(
            lambda size: it.repeat(size, 64),
            range(1,64)
        )
    )
)

def measure_test(test):
    """measures absolut error"""
    return abs(ref_median(*test)- median_tracker(*test).median())

print("sum(|error|)={error}".format(
    error=sum(
        map(
            measure_test,
            tests
        )
    )
))


