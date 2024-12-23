class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        current_sum=sum(nums[:k])
        maxsum=current_sum
        for i in range(k,n):
            current_sum+=nums[i]-nums[i-k]
            maxsum=max(maxsum,current_sum)
        return maxsum/k