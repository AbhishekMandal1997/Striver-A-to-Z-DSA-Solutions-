n = int(input())
def pyramid(n):
    for i in range(n + 1):
        for j in range(n,i,- 1):
            print(" ", end = "")
        for k in range((2 * i) - 1):
            print("*", end="")
        print()
pyramid(n)

