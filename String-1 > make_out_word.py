def make_out_word(s,n):
 return (s[:2]+n+s[2:])
s,n=input().split()
print(make_out_word(s,n))