def count_code(s):
 count=0
 for i in range(len(s)-4+1):
     if(s[i:i+2]=="co" and s[i+3]=="e"):
         count+=1
 return count

s=input()
print(count_code(s))
