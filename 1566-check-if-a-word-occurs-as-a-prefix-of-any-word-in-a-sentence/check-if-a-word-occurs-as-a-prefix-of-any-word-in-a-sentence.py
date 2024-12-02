class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i in range(len(sentence.lower().split())):
            if searchWord.lower() != " " and sentence.lower().split()[i].startswith(searchWord.lower()):
                return i+1

        return -1   
         

        