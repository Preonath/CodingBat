def max_end3(s):
    m=max(s[0],s[2])
    return (m,m,m)

s=input().split()
print(max_end3(s))