def count_even(nums):
    count=0
    for i in range(len(nums)):
        if(i%2==0):
            count+=1
    return count
num=input().split()
print(count_even(num))