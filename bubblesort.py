
# arr = [4,1,3,9,7]


# for j in range(len(arr)-1):
# 	for i in range(len(arr)-1):
# 		if arr[i+1] < arr[i]:
# 			temp = arr[i+1]
# 			arr[i+1] = arr[i]
# 			arr[i] = temp
# print(arr)


a = [7,8,9]

def minDist(arr, n, x, y):
	xidx = None
	for idx, val in enumerate(arr):
	    if val==x:
	        xidx = idx
	    if val==y:
	        yidx = idx
	        if xidx!=None:
	        	print(xidx, yidx)
	        	return yidx - xidx
	return -1

print(minDist([1,2], 2, 1,2))