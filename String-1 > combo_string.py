def combo_string(a,b):
    if(len(a)<len(b)):
        return(a+b+a)
    else:
        return(b+a+b)

s,n=input().split()
print(combo_string(s,n))