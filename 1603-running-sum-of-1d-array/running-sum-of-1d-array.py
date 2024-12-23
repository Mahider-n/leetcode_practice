class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum=[]
        final_sum=[]
        for i in range(len(nums)):
            runningSum.append(nums[i])
            r=sum(runningSum)
            final_sum.append(r)
        return final_sum
            

        