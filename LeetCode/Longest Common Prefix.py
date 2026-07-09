from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        res = ""
        first_word = strs[0]
        
        for i in range(len(first_word)):
            res += first_word[i]
            
            for string in strs:
                if i >= len(string) or string[i] != res[-1]:
                    # Remove that last letter from the end of res
                    res = res[:-1]
                    # Return the result immediately
                    return res
                    
        return res