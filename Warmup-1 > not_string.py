def not_string(str):
 if(len(str)>=3 and str[:3]=="not"):
     return (str)
 else:
     return("not"+" "+str)
s=input()
print(not_string(s))