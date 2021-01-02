


def twosum(arr, target):
	for i in range(len(arr)-1):
		for j in range(i+1,len(arr)):
			if (arr[i]+arr[j]) == target:
				print(i,j)
				return i, j 
	return 0

print(twosum([3,2,4], 6))