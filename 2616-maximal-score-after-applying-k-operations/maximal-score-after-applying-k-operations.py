class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # Create a max-heap using negative values
        pq = [-num for num in nums]
        heapq.heapify(pq)
        res = 0
        
        # Process for k iterations
        for _ in range(k):
            num = -heapq.heappop(pq)
            res += num
            newNum = (num + 2) // 3
            if newNum > 0:
                heapq.heappush(pq, -newNum)  # Push the reduced value back with negative sign
        
        return res