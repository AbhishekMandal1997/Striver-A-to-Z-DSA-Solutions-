n = int(input())
arr = list(map(int, input().split()))
def checkLargest(arr):
    largest = 0
    for i in arr:
        if i > largest:
            largest = i
    return largest 

print(checkLargest(arr))

