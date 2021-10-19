def sum67(nums):
 flag=True
 sum=0
 for i in range(len(nums)):
     if(nums[i]==6):
         flag=False
     elif flag==False and nums[i]==7:
         flag=True
     elif flag==True:
         sum+=nums[i]
 return sum


