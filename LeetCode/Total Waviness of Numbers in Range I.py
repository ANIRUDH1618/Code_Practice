class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        if num1/100 < 1 and num2/100 < 1:
            return 0
        waviness = 0
        for i in range(num1, num2 + 1):
            if i/100 < 1:
                continue
            waviness += check_peak_valley(str(i))

def check_peak_valley(val):
    waviness = 0
    
    for i in range(1, len(val) - 1):
        if int(val[i-1]) < int(val[i]) and int(val[i+1]) < int(val[i]):
            waviness += 1
            continue
        if int(val[i-1]) > int(val[i]) and int(val[i+1]) > int(val[i]):
            waviness += 1
            continue
        continue
    return waviness