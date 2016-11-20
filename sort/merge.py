from math import floor

def mergeSort(arr):
	arrLength = len(arr)
	if arrLength <= 1:
		return arr
	center = floor(arrLength/2)
	left = arr[0: center]
	right = arr[center: arrLength]
	return merge(mergeSort(left), mergeSort(right), arr)


def merge(left, right, arr):
	k = 0
	i = 0
	j = 0
	while (i < len(left) and j < len(right)):
		if left[i] <= right[j]:
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1
		k += 1
	while (i < len(left)):
		arr[k] = left[i]
		k += 1
		i += 1

	while (j < len(right)):
		arr[k] = right[j]
		k += 1
		j += 1

	return arr