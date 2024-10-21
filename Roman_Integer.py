class Solution:
    def romanToInt(self, s: str) -> int:
        Symbol = {
            'I' : 1 , 
            'V' : 5 ,
            'X' : 10 ,
            'L' : 50 ,
            'C' : 100 ,
            'D' : 500 ,
            'M' : 1000 ,
        }
        result = 0
        n = len(s)
        for i in range(n):
            if i < n -1 and Symbol[s[i]] < Symbol[s[i+1]]:
                result -= Symbol[s[i]]
            else:
                result += Symbol[s[i]]
        return result
        
s = Solution()
print(s.romanToInt("MCMXCIV"))