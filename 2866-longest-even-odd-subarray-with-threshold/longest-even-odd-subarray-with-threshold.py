class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        longest=0
        current=0
        for i in range(len(nums)):
            if nums[i]>threshold:
                current=0
            elif current==0 and nums[i]%2==0:
                current=1
            elif current >0 and nums[i]%2 != nums[i-1]%2:
                current+=1
            else:
                current=1 if nums[i] %2 ==0 else 0
            longest=max(longest,current)
        return longest 