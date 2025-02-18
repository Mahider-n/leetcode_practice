class Solution:
    def isPalindrome(self, x: int) -> bool:
        condition=False
        if(str(x)==str(x)[::-1]):
            condition=True 
        return condition 
        
         