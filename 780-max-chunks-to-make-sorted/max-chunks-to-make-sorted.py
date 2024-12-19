class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n=len(arr)
        max_value=0
        counteer=0
        for i in range(n):
            max_value=max(max_value,arr[i])
            if max_value==i:
                counteer+=1
        return counteer
        