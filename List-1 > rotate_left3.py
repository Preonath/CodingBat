def rotate_left3(nums):
    if(len(nums)==3):
        return [nums[1], nums[2], nums[0]]
    return False
s=input().split()
print(rotate_left3(s))