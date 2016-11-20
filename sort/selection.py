from utils import swap

def selectionSort(arr):
	arrLength = len(arr)
	# n = length of the array
	# outside loop n - 1 times
	for i in range(arrLength - 1):
		maximum = 0
		# since for in range in python will ignore the last element
		# (1, 7) will loop 1,2,3,4,5,6 without 7
		# so the range here is just arrLength - i
		for j in range(1, arrLength - i):
			if arr[j] > arr[maximum]:
				maximum = j

		# but the end of index should minus 1 a further step
		# i.e the first loop i = 0 arrlength = 7 the last item = 7 - 0 - 1
		# 2nd loop i = 1 arrlength = 7 the last item = 7 - 1 - 1
		swap(maximum, arrLength - i - 1, arr)
	return arr