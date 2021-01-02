def fact(n):
    facto = 1
    while(n>1):
        facto*=n
        n-=1
    return facto

def fact_rec(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

def perfect_num(num):
    sum_fact = 0
    temp_num = num
    while(num>0):
        dig = num%10
        sum_fact+=fact(dig)
        num//=10
    return "Perfect Number" if sum_fact==temp_num else "Not Perfect"

print(perfect_num(145))
