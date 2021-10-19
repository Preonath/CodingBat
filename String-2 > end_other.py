def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return (b.endswith(a) or a.endswith(b))
#https://www.w3schools.com/python/ref_string_endswith.asp
s,n=input().split()
print(end_other(s,n))
