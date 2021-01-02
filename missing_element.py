def missing_num(lst,n):
    sum_n = (n*(n+1))//2
    return sum_n - sum(lst)

for _ in range(int(input())):
    n = int(input())
    lst = [int(i) for i in input().split()]
    print(missing_num(lst,n))