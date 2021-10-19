def sum3(nums):
    if(len(nums)==3):
     sum=0
     for i in range(len(nums)):
        sum+=nums[i]
     return sum
    return False
s=input().split()
print(sum3(s))