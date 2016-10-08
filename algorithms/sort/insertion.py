from utils import swap

def insertionSort(arr):
	position = 1
	for position in range(len(arr)):
		for j in range(0, position):
			if arr[position] < arr[j]:
				temp = arr[position]
				arr.remove(arr[position])
				arr.insert(j, temp)
		position += 1
	return arr
