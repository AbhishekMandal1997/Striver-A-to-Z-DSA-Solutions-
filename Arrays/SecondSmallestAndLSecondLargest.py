
arr = list(map(int,input().split()))

def SecondLargestSecondSmallest(arr):
    arr.sort()
    smallest = arr[1]
    largest = arr[len(arr) - 2]

    print("Smallest Element: ",smallest)
    print("Largest Element: ", largest)

SecondLargestSecondSmallest(arr)