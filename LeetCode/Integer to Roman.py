
class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the symbol-value pairs in descending order
        value_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        res = ""
        
        # Iterate through the values
        for val, sym in value_map:
            # While the number is large enough, subtract and append
            while num >= val:
                res += sym
                num -= val
                
        return res