def xyz_there(s):
    for i in range(len(s)):
        if(s[i]!="." and s[i+1:i+4]=="xyz"):
            return True
    if(s[0:3]=="xyz"):
        return True
    return False
s=input()
print(xyz_there(s))
