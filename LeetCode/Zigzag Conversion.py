class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        res = [[] for _ in range(numRows)]

        a = 0
        top = True
        
        for i in range(len(s)):
            res[a].append(s[i])
            
            # Logic to change rows
            if top:
                a += 1
                if a == numRows - 1:
                    top = False
            else:
                a -= 1
                if a == 0:
                    top = True
        
        result = ''

        for row in res:
            for char in row:
                result += char  # Concatenate instead of append

        return result

def main():
    res = Solution()
    output = res.convert('abcdefghijklm', 3)
    print(output)

if __name__ == "__main__":
    main()