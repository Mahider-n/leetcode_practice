class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        counter=0
        for i in range(n):
            if nums[i]>nums[(i+1) %n]:
                counter+=1
            if counter >1:
                return False 
        return True 
        