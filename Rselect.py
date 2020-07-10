

import numpy as np

def Rselect(array, i):
	if i > len(array):
		raise Exception
	n = len(array)
	if n == 1:
		return array[0]

	k = int(np.random.uniform(0,n))
	pivot = array[k]

	part_a, part_b, pivots = partition(array, pivot)
	# print part_a, part_b, pivots

	j = len(part_a)
	part_b =  pivots[1:] + part_b
	if i == j+1:
		return pivot
	elif i > j+1:
		return	Rselect(part_b, i-j)
	elif i < j+1:
		return Rselect(part_a, i)


def partition(array, pivot):
	part_a, part_b, pivots = [], [], []

	for i in array:
		if i < pivot:
			part_a.append(i)
		elif i > pivot: 
			part_b.append(i)
		else:
			pivots.append(i)

	return part_a, part_b, pivots


a = [1,7,4,2,9,4,6,7,9,10,0]

print a
# print Rselect(a,0)
for i in range(1,10):
	print i ,Rselect(a,i)