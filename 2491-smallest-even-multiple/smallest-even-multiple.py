class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        result=0
        y=n*2
        if(n>=1):
            if(n%2==0):
                result=n
            elif(y%2==0):
                result=y

        return result 
        
                

        