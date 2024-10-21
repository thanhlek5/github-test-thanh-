from typing import List
def maxArea( height: List[int]) -> int:
        area = 0
        left= 0
        right = len(height) - 1
        while left < right:
            r = min(height[left],height[right])
            l = right - left
            area = max(area,l*r)
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return area
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))