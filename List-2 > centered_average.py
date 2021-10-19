def centered_average(nums):
    count=sum(nums)
    return((count-max(nums)-min(nums))/(len(nums)-2))