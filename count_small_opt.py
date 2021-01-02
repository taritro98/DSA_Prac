def count_sm(lst,key):
    return sum(elem<=key for elem in lst)
    
def count_sm_opt(lst, key):
    low=0
    high=len(lst)-1
    count = 0
    mid=0
    while(low<=high):
        mid = (low+high)//2
        if lst[mid]<=key:
            count=mid+1
            low=mid+1
        else:
            high=mid-1
    return count


if __name__=='__main__':
    a = int(input())
    for i in range(a):
        n = int(input())
        lst = [int(i) for i in input().split()]
        key = int(input())
        print(count_sm_opt(lst,key))