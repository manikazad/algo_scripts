__author__ = "Manik"

import numpy as np
import time
count = 0

def quick_sort(array):
    #global count 
    #count +=1
    #if count < 20:
    n = len(array)
    if n  == 1:
        return array
    
    i = int(np.random.uniform(0,n))
    pivot = array[i]
    part_a, part_b, pivots = partition(array, pivot)
    
    if part_a:
        part_a = quick_sort(part_a)
    
    if part_b:
        part_b = quick_sort(part_b)
    
    return part_a + pivots + part_b
    
    
def partition(array, pivot):
    part_a, part_b, pivots = [], [], []
    for n in array:
        if n < pivot:
            part_a.append(n)
        elif n > pivot:
            part_b.append(n)
        else:
            pivots.append(n)
    return part_a, part_b, pivots


a = [1,7,4,2,9,4,6,7,9,10,0]
print a
t1 = time.time()
print quick_sort(a)
print "time taken: ", time.time()-t1