# def array123(nums):
#     sub=[1,2,3]
#     if(len(nums)!=0):
#      for i in range(len(nums)):
#         s=nums[i:i+3]
#         if(s==sub):
#             return True
#         else:
#             return False
#     else:
#         return False
def array123(nums):
    for  i in range(len(nums)-2):
        if(nums[i]==1 and nums[i+1]== 2 and nums[i+2]==3):
            return True
    return  False
s=input().split()
print(array123(s))
