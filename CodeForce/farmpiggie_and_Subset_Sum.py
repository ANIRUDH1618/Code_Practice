import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    t = int(next(iterator))
    out = []

    for _ in range(t):
        n = int(next(iterator))
        res = [str(i + 1 if i % 2 == 1 else i - 1) for i in range(1, n + 1)]
        out.append(" ".join(res))

    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    solve()