import math

def getPermutation(self, n: int, k: int) -> str:
    s=[]
    for i in range(n):
        s.append(str(i+1))
    
def fun(s,k,l):
    p=[]
    fact=math.factorial(l)
    #print(fact)
    while (s!=[]): 
        fact=fact//l
        #print(fact)
        i,k=divmod(k,fact)
        #print(i,k)
        x=s[i] 
        p.append(x) 
        s=s[:i]+s[i+1:]
        #print(s)
        l-=1
        #print(p)
        return "".join(p)
        
    return fun(s,k-1,n)
