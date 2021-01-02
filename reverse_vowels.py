

def isVowel(c):
    return c == 'a' or c == 'A' or c == 'e' or c == 'E' or c == 'i' or c == 'I' or c == 'o' or c == 'O' or c == 'u' or c == 'U'

def vow_rev(st):
    vow = []
    st = list(st)
    for i in range(len(st)):
        if isVowel(st[i]):
            vow.append(st[i])
    
    ln = len(vow)   
    for i in range(len(st)):
        if isVowel(st[i]):
            st[i] = vow[ln-1]
            ln-=1
    return "".join(st)
    
def vow_rev_opt(st):
    i=0
    j=len(st)-1
    while(i<j):
        if not isVowel(st[i]):
            i+=1
            continue
        
        if not isVowel(st[j]):
            j-=1
            continue
        
        st[i], st[j] = st[j], st[i]
        i+=1
        j-=1
        
    return "".join(st)
    
if __name__=='__main__':
    a = int(input())
    for i in range(a):
        st = input()
        print(vow_rev_opt(list(st)),sep="")