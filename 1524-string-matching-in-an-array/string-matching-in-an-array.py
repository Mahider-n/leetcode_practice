from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for i, word in enumerate(words):
            # Check if the current word is a substring of any other word
            for j, other_word in enumerate(words):
                if i != j and word in other_word:
                    result.append(word)
                    break  # No need to check further once the word is found as a substring
        return result

        #        if words[i] in words[i+1]:
        #         result.append(words[i])
        #     if words[i+1] in words[i]:
        #         result.append(words[i+1])
             
        # return result
           
        # for element in words[1:]: 
            # if target in element:
            #     result.append(target)
            #     return result
           
        
 