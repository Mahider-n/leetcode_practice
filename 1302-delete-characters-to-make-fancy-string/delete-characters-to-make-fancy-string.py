class Solution:
    def makeFancyString(self, s: str) -> str:
        
        if len(s) < 3:
            return s
        
        
        chars = list(s)
        j = 2
         
        for i in range(2, len(s)):
            
            if chars[i] != chars[j-1] or chars[i] != chars[j-2]:
                chars[j] = chars[i]
                j += 1
         
        return ''.join(chars[:j])
        