def rev_num(num):
    rev = 0
    while(num>0):
        rev = rev*10 + num%10
        num = num//10
    return rev

def isPalin(num):
    return (rev_num(num)==num)

def func(num):
    i = 0
    rev_number=0
    rev_sum = num
    while(i<=5):
        if isPalin(rev_sum):
            return rev_sum
        rev_number = rev_num(num)
        rev_sum = num+rev_number
        num=rev_sum
        i+=1
    return -1

for _ in range(int(input())):
    a = int(input())
    print(func(a))
            