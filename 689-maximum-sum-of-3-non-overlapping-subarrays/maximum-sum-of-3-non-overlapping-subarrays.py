class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)
        # Compute the sum of all subarrays of length k
        sum_k = [0] * (n - k + 1)
        current_sum = sum(nums[:k])
        sum_k[0] = current_sum
        for i in range(1, len(sum_k)):
            current_sum += nums[i + k - 1] - nums[i - 1]
            sum_k[i] = current_sum
        
        # Compute left array
        left = [0] * len(sum_k)
        best_left = 0
        for i in range(len(sum_k)):
            if sum_k[i] > sum_k[best_left]:
                best_left = i
            left[i] = best_left
        
        # Compute right array
        right = [0] * len(sum_k)
        best_right = len(sum_k) - 1
        for i in range(len(sum_k) - 1, -1, -1):
            if sum_k[i] >= sum_k[best_right]:
                best_right = i
            right[i] = best_right
        
        # Find the best combination
        max_sum = 0
        result = []
        for mid in range(k, len(sum_k) - k):
            l = left[mid - k]
            r = right[mid + k]
            total = sum_k[l] + sum_k[mid] + sum_k[r]
            if total > max_sum:
                max_sum = total
                result = [l, mid, r]
        
        return result

 
