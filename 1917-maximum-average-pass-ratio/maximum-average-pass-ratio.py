import heapq

class Solution:
    def maxAverageRatio(self, classes, extraStudents):
        # Calculate initial impact and populate max heap
        heap = []
        for passi, totali in classes:
            # Max heap needs negative impact
            impact = (passi + 1) / (totali + 1) - (passi / totali)
            heapq.heappush(heap, (-impact, passi, totali))
        
        # Assign extra students to classes
        for _ in range(extraStudents):
            impact, passi, totali = heapq.heappop(heap)
            # Update the class with one more passing student
            passi += 1
            totali += 1
            new_impact = (passi + 1) / (totali + 1) - (passi / totali)
            heapq.heappush(heap, (-new_impact, passi, totali))
        
        # Calculate the final average pass ratio
        total_ratio = 0
        for _, passi, totali in heap:
            total_ratio += passi / totali
        
        return total_ratio / len(classes)

# Example usage:
solution = Solution()

classes1 = [[1, 2], [3, 5], [2, 2]]
extraStudents1 = 2
print(solution.maxAverageRatio(classes1, extraStudents1))  # Output: 0.78333

classes2 = [[2, 4], [3, 9], [4, 5], [2, 10]]
extraStudents2 = 4
print(solution.maxAverageRatio(classes2, extraStudents2))  # Output: 0.53485
