import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        k = int(input_data[idx])
        idx += 1
        
        no_of_alpabet = [int(x) for x in input_data[idx : idx + k]]
        idx += k
        
        no_of_letter = sum(1 for c in no_of_alpabet if c >= 2)
        max_count = max(no_of_alpabet)
        
        if max_count >= 3 or no_of_letter >= 2:
            out.append("YES")
        else:
            out.append("NO")
            
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()