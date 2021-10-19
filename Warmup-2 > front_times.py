def front_times(str,n):
    r=""
    n=int(n)
    for i in range(n):
        r+=str[:3]
    return r
s,n=input().split()
print(front_times(s,n))
