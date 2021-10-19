def array_front9(nums):
    en=nums[:4]
    for i in en:
        if i== 9:
            return True
        else:
            return False
s=input().split()
print(array_front9(s))