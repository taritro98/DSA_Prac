def fact(i):
    if i==1:
        return 1
    else:
        return i*fact(i-1)


def countdown(i):
    print(i)
    if i<=0:
        return
    else:
        countdown(i-1)

def sum(arr):
    for elem in arr:
        if arr == []:
            return 0
        else:
            return elem*arr.pop[elem]

print(sum([1,2,3]))