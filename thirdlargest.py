def thirdLargest(arr):
    x = max(arr)
    arr.pop(arr.index(x))
    maxval = 0
    for a in arr:
        if a>maxval:
            maxval = a
    arr.pop(arr.index(maxval))
    maxval = 0
    for a in arr:
        if a>maxval:
            maxval = a
    return maxval

print(thirdLargest([2,4,1,3,5]))