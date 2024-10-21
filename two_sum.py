# ĐÃ HOÀN THÀNH ++++
def two_sum(nums,target):
    for i in range(len(nums)):
        n = target - nums[i] 
        for j in range(len(nums)):
            if nums[j]==n and i!=j:
                return i,j
list=[50,23,43,45,54,20] #target = 9
print(two_sum(list,99))

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.