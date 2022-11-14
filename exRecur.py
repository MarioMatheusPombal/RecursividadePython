def fat(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fat(n-1)

print(fat(4))

def exp(v1,v2):
    if v2 == 0:
        return 1
    else:
        return(v1*exp(v1,v2-1))
 
print(exp(2,4))

def mult(x,y):
    if x == 0 or y==0:
        return 0
    elif x == 1:
        return y
    elif y == 1:
        return x
    else:
        return x + mult(x,y-1)

print(mult(2,4))

def fibo(n):
    if n == 1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(8))

