class Solution:
    def productExceptSelf(self, nums: list[int]):
        n = len(nums)
        products = [1]*n
        for i in range(1,n):
            products[i] = products[i-1]* nums[i-1]
        right = nums[-1]
        for i in range(n-2,-1,-1):
            products[i] = right*products[i]
            right *= nums[i]
        return products
nums = [1,2,3,4]
s = Solution()
print(s.productExceptSelf(nums))