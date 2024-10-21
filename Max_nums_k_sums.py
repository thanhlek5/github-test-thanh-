from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        i =0
        while i < len(nums):
            j = k - nums[i]
            count_of_left = nums.count(j)
            count_of_right = nums.count(nums[i])
            count = min(count_of_left,count_of_right)
            nums.pop(nums.index(j))
            nums.pop(i)
            
            
            
        return count
s = Solution()
nums = [1,2,3,4]
k = 5
print(s.maxOperations(nums,k))
