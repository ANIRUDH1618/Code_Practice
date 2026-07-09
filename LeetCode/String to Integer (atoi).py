class Solution:
    def myAtoi(self, s: str) -> int:
        if not (0 <= len(s) <= 200):
            return 0
            
        notnum = True
        a = ''
        
        for i in range(len(s)):
            # If we haven't started reading a number yet
            if notnum:
                if s[i] == " ":
                    continue
                elif s[i] == '-' or s[i] == '+':
                    a += s[i]
                    notnum = False
                elif s[i].isdigit():
                    a += s[i]
                    notnum = False
                else:
                    # Any other character before a number is invalid
                    break
            
            # If we are currently reading a number
            else:
                if s[i].isdigit():
                    a += s[i]
                    notnum = False
                else:
                    break
                    
        # Handle cases where 'a' is empty or just a sign
        if a == '' or a == '-' or a == '+':
            return 0

        # Convert to integer
        res = int(a)
        
        # Clamp to 32-bit signed integer limits
        if res < -2147483648:
            return -2147483648
        if res > 2147483647:
            return 2147483647
            
        return res