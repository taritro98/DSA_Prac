def smallest(arr):
    smallest_idx = 0
    smallest_no = arr[0]
    for i in range(1,len(arr)):
        if arr[i]<smallest_no:
            smallest_no = arr[i]
            smallest_idx=i
    return smallest_idx

def selection_sort(arr):
    newarr = []
    for i in range(len(arr)):
        smallest_elem=smallest(arr)
        newarr.append(arr.pop(smallest_elem))
    return newarr

print(selection_sort([3,5,6,7,8,2,15,17,42,1,0,4,3,2]))
