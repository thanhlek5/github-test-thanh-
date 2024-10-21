# 1     1     1             2       2       2
# 1     1     0     ==>     2       2       0
# 1     0     1             2       0       1
# color = 2  ,sr = 1 , sc = 1
# image[sr][sc]

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        prev_color =image[sr][sc] 
        if prev_color != color:
            self.fill(image,sr,sc,color,image[sr][sc])
            return image
        
    def fill(self, image: list[list[int]], sr: int, sc: int, color: int,prev_color: int) -> list[list[int]]:
        if sr <0 or sc <0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != prev_color:
            return
        image[sr][sc] = color
        self.fill(image,sr-1,sc,color,prev_color)
        self.fill(image,sr+1,sc,color,prev_color)
        self.fill(image,sr,sc-1,color,prev_color)
        self.fill(image,sr,sc+1,color,prev_color)
s = Solution()
image = [[0,0,0],[0,0,0]]; sr = 0; sc = 0; color = 0
print(s.floodFill(image,sr,sc,color))
