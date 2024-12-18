class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer=prices[:]
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    answer[i]-=prices[j]
                    break
        return answer

        