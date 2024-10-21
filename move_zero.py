def moveZeroes( nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[zero] = nums[i]
                zero += 1
        for i in range(zero,len(nums)):
            nums[i]=0
        return nums
    
nums = [0,1,0,3,12]
print(moveZeroes(nums))