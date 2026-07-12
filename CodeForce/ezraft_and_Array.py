import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        if n == 1:
            results.append("1")
        elif n == 2:
            results.append("-1")
        else:
            ans = [1, 2, 3]
            current_sum = 6
            for _ in range(4, n + 1):
                ans.append(current_sum)
                current_sum *= 2
            results.append(" ".join(map(str, ans)))
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    solve()