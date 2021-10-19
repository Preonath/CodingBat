def front3(str):
    if(len(str)<1):
        return str
    else:
        return (str[0:3]+str[0:3]+str[0:3])
s=input()
print(front3(s))
