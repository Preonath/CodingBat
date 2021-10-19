def array_count9(nums):
    r=0
    for i in nums:
        if(i==9):
         r+=1
    return r
s=input().split(",")
print(array_count9(s))