n = int(input())
def solve(n):
    for i in range(n + 1):
        for j in range(i):
            print("*", end = " ")
        print()
    for i in range(n - 1, 0 , -1):
        for j in range(i):
            print("*", end = " ")
        print()
solve(n)