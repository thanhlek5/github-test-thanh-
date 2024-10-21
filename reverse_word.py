class Solution:
    def reverseWords(self, s: str) -> str:
        # tạo list cách nhau bằng space 
        ls_s = s.split()
        # taoj biến để chạy từ phải và trái 
        r, l = 0, len(ls_s) - 1
        # đổi vị trí đầu cuối từ ngoài vào trong 
        while r < l:
            ls_s[r], ls_s[l] = ls_s[l], ls_s[r]
            r += 1
            l -= 1
        # biến từ list lại thành chuỗi 
        return ' '.join(ls_s)