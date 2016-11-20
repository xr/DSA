# from utils import swap

# def quickSort(arr):
# 	return quickSortRec(arr, 0, len(arr) - 1)

# def quickSortRec(arr, start, end):
# 	if start < end:
# 		pIndex = partition(arr, start, end)

# 		quickSortRec(arr, start, pIndex - 1)
# 		quickSortRec(arr, pIndex + 1, end)
# 		return arr

# def partition(arr, start, end):
# 	pivot = arr[end]
# 	pIndex = start
# 	for i in range(start, end):
# 		# since we choose the last element as the pivot
# 		# thus, we need to swap all the element that less than pivot to the left
# 		if arr[i] <= pivot:
# 			swap(i, pIndex, arr)
# 			pIndex += 1
# 	swap(end, pIndex, arr)
# 	return pIndex

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)
   return alist

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark