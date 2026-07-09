class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # check for odd palindrome
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            odd_pal = s[left + 1 : right]
        
            if len(odd_pal) > len(res):
                res = odd_pal
        
            # check for even palindrom
            left = i
            right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            even_pal = s[left + 1 : right]
        
            if len(even_pal) > len(res):
                res = even_pal
        
        return res
    
    