class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O','U']
        r = 0
        l = len(s) -1
        lis_s = list(s)
        while r < l :
            if lis_s[r] in v and lis_s[l] in v:
                lis_s[r] , lis_s[l] = lis_s[l] , lis_s[r]
                r +=1
                l -=1
            elif lis_s[r] not in v:
                r+=1
            elif lis_s[l] not in v:
                l -=1
        return "".join(lis_s)
                