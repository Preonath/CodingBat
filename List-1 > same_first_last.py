def same_first_last(nums):
    if(len(nums)>=1):
     if(nums[0]==nums[-1]):
         return True
     else:
         return False
    else:
        return False
s=input().split()
print(same_first_last(s))