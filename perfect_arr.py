

def rev_arr_without_slice(lst):
    low = 0
    high = len(lst)-1
    for i in range(len(lst)//2):
        lst[low],lst[high] = lst[high], lst[low]
        low+=1
        high-=1
    return lst


def rev_arr(lst):
    return "PERFECT" if (lst==lst[::-1]) else "NOT PERFECT"

for _ in range(int(input())):
    n = int(input())
    lst = [int(i) for i in input().split()]
    print(rev_arr_without_slice(lst))