def last2(str):
    c=0
    for i in range(len(str)-2):
        sub=str[i:i+2]
        if(sub==str[-2:]):
            c+=1
    return c
s=input()
print(last2(s))