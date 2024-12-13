from typing import List

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, 0
        n = len(nums)
        greatness = 0
        while i < n and j < n:
            if nums[j] > nums[i]:
            # Found a valid perm[j] > nums[i]
                greatness += 1
                i += 1  # Move to the next index in nums
            j += 1  # Always move the perm pointer
    
        return greatness