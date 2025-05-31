#Q1

"""
def sum(n):
    if n<10:
        return n
    else:
        return sum(n//10)+(n%10)
x=sum(853)
print(x)


#Q2
def fac(x):
    if x==1:
        return 1
    else:
        return fac(x-1)*x
print(fac(6))



#Q3
def change(x):
    if x==1:
        return 1
    else:
        return(str(change(x//2))+str(x%2))
print(int(change(15)))




#Q4
def change(x):
    if x<8:
        return x%8
    else:
        return(str(change(x//8))+str(x%8))
print(int(change(45)))

"""

#Q5

def sum(n):
    if n==1:
        return 2
    else:
        return (sum(n-1)+term(n))
def term(m):
    i=0
    x=2
    c=0
    while i<m:
        for e in range(2,x):
            if x%e==0:
                x+=1
                break
        else:
            c=x
            i+=1
            x+=1

    return c
print(sum(5))














