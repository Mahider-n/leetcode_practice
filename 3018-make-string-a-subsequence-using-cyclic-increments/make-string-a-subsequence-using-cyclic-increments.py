class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n, m = len(str1), len(str2)
        j = 0
        for i in range(n):
            if j < m and str1[i] == str2[j]:
                j += 1
            elif j < m and (ord(str1[i]) + 1 - ord('a')) % 26 + ord('a') == ord(str2[j]):
                j += 1

        return j == m