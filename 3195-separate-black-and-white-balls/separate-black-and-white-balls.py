class Solution:
    def minimumSteps(self, s: str) -> int:
        b_count,swap=0,0
        for n in s:
            if n=='0':
                swap+=b_count
            else:
                b_count+=1
        return swap
        