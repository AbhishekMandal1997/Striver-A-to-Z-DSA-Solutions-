n = int(input())
def squareBox(n):
    for i in range(n):  
        for j in range(n): 
            print("*", end = " ")
        print()
squareBox(n)
