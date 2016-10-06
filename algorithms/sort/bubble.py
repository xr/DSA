def sort(arr):
    arrLengh = len(arr)
    end = arrLengh - 1
    while end > 0:
        for i in range(arrLengh):
            if i < arrLengh - 1:
                if arr[i] > arr[i + 1]:
                    swap(i, i + 1, arr)
        end -= 1
    return arr

def swap(a, b, arr):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return arr