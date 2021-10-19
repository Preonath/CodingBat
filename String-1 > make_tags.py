def make_tags(tag, word):
 return ("<"+tag+">"+word+"</"+tag+">")
s,n=input().split()
print(make_tags(s,n))