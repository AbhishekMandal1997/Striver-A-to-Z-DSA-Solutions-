n = int(input())
def solve(n):
    for i in range(n + 1):
        for j in range(i):
            print(i, end = " ")
        print()
solve(n)


