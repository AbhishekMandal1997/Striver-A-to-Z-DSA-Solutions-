n = int(input())
n=n*2
def numberCrown(n):
    for i in range(n):
        for j in range(i):
            print(i,end = "") 
        print()
numberCrown(n)