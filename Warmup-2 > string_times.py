def string_times(str,n):
    n=int(n)
    r=""
    for i in range(n):
        r+=str
    return r
s,n=input().split()
print(string_times(s,n))