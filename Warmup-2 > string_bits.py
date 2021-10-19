def string_bits(str):
    r=""
    for i in range(len(str)):
        if(i%2==0):
            r+=str[i]
    return r
s=input()
print(string_bits(s))