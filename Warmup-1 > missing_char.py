def missing_char(str, n):
 n=int(n)
 front=str[0:n]
 back=str[n+1:]
 return(front+back)
s,n=input().split()
print(missing_char(s,n))