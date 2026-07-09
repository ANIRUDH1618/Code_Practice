class Solution:
    def lengthOfLongestSubstring(self, s: str):
        result = []
        temp = []
        for i in range(len(s)):
            if i == 0:
                temp.append(s[i])
                
            else:
                x, a = check_similar(temp, s[i])
                if x:
                    if len(result)>len(temp):
                        temp = a
                        temp.append(s[i])
                    else:
                        result = temp
                        temp = a
                        temp.append(s[i])
                else: 
                    temp.append(s[i])
                    
        
        if len(temp) > len(result):
            result = temp.copy()
        return len(result)

                    
def check_similar(arr, character):
    if character in arr:
        idx = arr.index(character)
        after = arr[idx + 1 : ] 
        return True, after
        
    return False, None
            


