from utils import swap

def bubbleSort(arr):
    arrLengh = len(arr)
    end = arrLengh - 1
    while end > 0:
        for i in range(arrLengh):
            if i < arrLengh - 1:
                if arr[i] > arr[i + 1]:
                    swap(i, i + 1, arr)
        end -= 1
    return arr