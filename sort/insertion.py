from utils import swap

def insertionSort(arr):
	position = 1
	for position in range(len(arr)):
		# EDIT: avoid the following implementation
		# if so, the best case is still O(n^2)
		# for j in range(0, position):
		# 	if arr[position] < arr[j]:
		# 		temp = arr[position]
		# 		arr.remove(arr[position])
		# 		arr.insert(j, temp)
		# position += 1
		j = position
		while ( j != 0) and (arr[j] < arr[j - 1]):
			swap(j, j - 1, arr)
			j -= 1
	return arr
