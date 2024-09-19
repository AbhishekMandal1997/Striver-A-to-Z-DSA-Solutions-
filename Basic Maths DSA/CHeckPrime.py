N = int(input())

def checkPrime(N):
    count = 0
    for i in range(1,N + 1):
        if N % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False
if checkPrime(N):
    print("It is a Prime Number")
else:
    print("It is not a Prime Number")
