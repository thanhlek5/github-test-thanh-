# ĐÃ HOÀN THÀNH ++++
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        fisrt = 0 
        last = len(nums) -1 
        while fisrt <= last:
            mid = int((fisrt + last)/2)
            if nums[mid] < target:
                fisrt = mid +1
            elif nums[mid] > target:
                last = mid =1
            else:
                return mid
        return -1
                
nums = [-1,0,3,5,9,12]
target = 2
s = Solution()

print(s.search(nums,target))
