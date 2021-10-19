def front_back(str):
  if(len(str)<=1):
      return str
  else:
      mid=str[1:len(str)-1]
      first=str[len(str)-1]
      last=str[0]
      return(first+mid+last)
s=input()
print(front_back(s))

