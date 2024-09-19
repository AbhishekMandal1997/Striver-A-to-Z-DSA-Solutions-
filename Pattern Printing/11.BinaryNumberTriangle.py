n = int(input())
def BinaryNumberTriangle(n):
    for i in range(n + 1):
        for j in range(i):
            if j % 2 == 0:
                print(1,end= " ")
            else:
                print(0,end = " ")
        print()
BinaryNumberTriangle(n)