class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        return (f:=lambda s,d=set():s and max((t:=s[:i+1]) not in d and (d.add(t),f(s[i+1:]),d.remove(t))[1] for i in range(len(s))) or len(d))(s)
        