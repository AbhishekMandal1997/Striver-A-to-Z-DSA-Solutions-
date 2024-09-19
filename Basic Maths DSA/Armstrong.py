n = int(input())

def CheckArmstrong(n):
    dup = n
    sum = 0
    power = len(str(n))

    while dup > 0:
        digit = dup % 10
        sum += digit ** power
        dup = dup // 10
    if sum == n:
        print("True")
    else:
        print("False")

CheckArmstrong(n)