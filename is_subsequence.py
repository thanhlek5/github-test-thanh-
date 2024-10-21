def isSubsequence(s: str, t: str):
        k = 0
        t = list(t)
        for i in range(len(s)):
            found = False
            for j in range(k,len(t)):
                if s[i] == t[j] and k <= j:
                    found = True 
                    k = j
                    t.pop(j)
                    break
                print(k)
        
        if not found:
            return False
        return True 
s = "bb"
t = "ahbgdc"
print(isSubsequence(s,t))