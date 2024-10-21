class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # tìm ước chung lớn nhất bằng thuật toán euclid
        #     vd:Tính GCD của 48 và 18:
        # 48 % 18 = 12 (phần dư)
        # Gán a = 18, b = 12
        # 18 % 12 = 6 (phần dư)
        # Gán a = 12, b = 6
        # 12 % 6 = 0 (phần dư)
        # Gán a = 6, b = 0
        # Khi b = 0, kết quả là a = 6, tức là GCD của 48 và 18 là 6.
        def gdc(a,b):
            while b:
                a,b = b, a%b
                return a
        if str1 + str2 != str2 +str1 :
            return ""
        else: 
            return str1[:gdc(len(str1),len(str2))]