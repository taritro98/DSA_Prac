# def tripletsum(arr):
# 	for idx, pointer1 in enumerate(arr):
# 		arr.pop(idx)
# 		for idx2 in range(len(arr)-1):
# 			for idx3 in range(idx2+1,len(arr)):
# 				if pointer1+arr[idx2]+arr[idx3] == 0:
# 					return True
# 	return False

def tripletsum(arr, n):
	for i in range(n-1):
		s = set()
		for j in range(i+1, n):
			x = -(arr[i] + arr[j])
			if x in s:
				return True
			else:
				s.add(arr[j])
	return False

print(tripletsum([0, -1, 2, -3, 1], 5))
#print(tripletsum([1, 2, 3], 3))