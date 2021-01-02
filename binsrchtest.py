def binarysearch(arr, n, k):
	low = 0
	high = n
	while low<=high:
		mid=(low+high)//2
		if k==arr[mid]:
			return mid
		elif k>arr[mid]:
			low=mid+1
		else:
			high = mid-1

print(binarysearch([1,2], 2 ,2 