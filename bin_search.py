import sys

a = [1,3,4,5,2,6,8,7,9,10,16,45]
a.sort()
print(a)

to_search = int(sys.argv[1])

low = 0
high = len(a) - 1
mid = high+low//2

while low<=high:
    mid = high+low//2
    if to_search==a[mid]:
        print(mid)
    if to_search>a[mid]:
        low=mid+1
    else:
        high=mid-1