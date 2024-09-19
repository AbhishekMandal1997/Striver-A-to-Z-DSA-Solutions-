n = int(input())
dup = n
def ReverseDigit(n):
    Reverse = 0

    while n != 0:
        remainder = n % 10
        Reverse = (Reverse * 10) + remainder
        n //= 10
    if Reverse == dup:
        return "Palindrome Number"
    else:
        return "Not a Palindrome Number"
print(ReverseDigit(n))
