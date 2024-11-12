class Solution:
    def isCircularSentence(self, s: str) -> bool:
        m, n = 0, len(s)
        
        while m < n:
            while m + 1 < n and s[m + 1] != ' ':
                m += 1
            if m + 1 >= n:
                break
            if s[m] != s[m + 2]:
                return False
            m += 2

        return s[0] == s[n - 1]