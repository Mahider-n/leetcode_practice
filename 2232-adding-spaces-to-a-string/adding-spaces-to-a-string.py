class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        last_index = 0
        for  index in spaces:
            result.append(s[last_index:index])
            result.append(' ') 
            last_index = index 
        result.append(s[last_index:])
        return ''.join(result)
        