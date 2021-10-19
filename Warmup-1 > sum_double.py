def sum_double(a, b):
    a=int(a)
    b=int(b)
    if a!=b:
     return(a+b)
    elif(a==b):
        return(2*(a+b))
a,b = input().split()
print(sum_double(a,b))