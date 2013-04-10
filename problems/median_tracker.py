from __future__ import print_function
import heapq as h
import utils
import collections  as c
import operator as op
import random as rndm
import itertools as it
import functools as ft

class median_tracker(object):
    """
    tracks medians of the appended numbers
    by having ``equally'' sized min- and maxheap pair.
    [max_heap] + [min_heap] and to get median we access need (at most)
    access the biggest element in max_heap and smallest element in min_heap

    min_heap = contains the bigger half
    max_heap = contains the smaller half

    median = O(1)
    append = O(log(n)) (per element)
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
        return -h.heappop(self.max_heap)
    def len_min(self):
        return len(self.min_heap)
    def len_max(self):
        return len(self.max_heap)
    def get_min(self): #NOTE will only return the smallest element in the biggest half
        return self.min_heap[0]
    def get_max(self): #NOTE will only return the biggest element in the smallest half
        return -self.max_heap[0]
    def view_min(self):
        return str(sorted(self.min_heap))
    def view_max(self):
        return str(list(reversed(list(map(op.neg, sorted(self.max_heap))))))

    def append(self, *elems):
        #print("append({elems})".format(elems=elems))
        list(map(self.append_elem, elems))
    def append_elem(self, elem):
        #print("append_elem({elem})".format(elem=elem))
        #start cases, cannot simply put this logic in the logic 
        #that follows, the smaller half is the default half
        if(self.len_min()==0 and self.len_max()==0):
            self.push_max(elem)
            return

        #decide where to put it
        if(elem<self.get_max()): 
            #fits in the smallest half
            self.push_max(elem)
        elif(self.len_min()==0 or elem>=self.get_min()): 
            #fits in the biggest half
            self.push_min(elem)
        else:
            #doesn't matter
            self.push_max(elem)

        #rebalance the heaps #NOTE can only be unbalanced by one 
        if(abs(self.len_max()-self.len_min())>1): 
            #unbalanced, let's go ``robin hood''
            if(self.len_min()<self.len_max()):
                self.push_min(self.pop_max()) 
            elif(self.len_max()<self.len_min()):
                self.push_max(self.pop_min()) 
            else:
                raise Exception()

    def __str__(self):
        """shows both heaps flatted out with each others roots touching"""
        return "{max_heap}|{min_heap}".format(
            max_heap=self.view_max(), 
            min_heap=self.view_min()
        )
    def __repr__(self):
        return self.__str__()

    def median(self):
        """O(1)"""
        if( self.len_min()+self.len_max()==0 ): #has elements at all
            raise Exception()
        elif( self.len_min()==self.len_max() ):
            return float(self.get_min()+self.get_max())/2 
        elif( self.len_min()<self.len_max() ):
            return float(self.get_max()) 
        elif( self.len_max()<self.len_min() ):
            return float(self.get_min())
        else:
            raise Exception()

ref_median = utils.median

def random_list(size, domain=(-2,2)):
    return (rndm.uniform(domain[0], domain[1]) for i in range(size))

testsuite_size = 10
max_test_size = 1000

tests = map(
    random_list,
    it.chain.from_iterable(
        map(
            lambda size: it.repeat(size, testsuite_size),
            range(1,max_test_size)
        )
    )
)

def measure_test(test):
    """measures absolut error"""
    test = list(test)
    ref = ref_median(*test) 
    tracker = median_tracker(*test)
    tracker_median = tracker.median() 
    err = abs(ref-tracker_median)
    if(err>0.0001):
        print(ref,"vs.",tracker_median)
    return err

print("sum(|error|)={error}".format(
    error=sum(
        map(
            measure_test,
            tests
        )
    )
))

