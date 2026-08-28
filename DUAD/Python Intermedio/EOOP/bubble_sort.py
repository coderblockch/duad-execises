def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


numbers = [5, 2, 8, 1, 9, 3]
print("Before:", numbers)
print("After:", bubble_sort(numbers))