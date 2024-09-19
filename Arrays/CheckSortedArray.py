arr = list(map(int,input().split()))

def checkSortedArray(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

print(checkSortedArray(arr))
