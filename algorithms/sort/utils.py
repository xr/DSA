def swap(a, b, arr):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return arr