def makes10(a,b):
    a=int(a)
    b=int(b)
    if a==10 or b==10:
        return True
    elif(a!=0 or b!=10):
        if(a+b==10):
            return True
        else:
            return False
a,b = input().split()
print(makes10(a,b))