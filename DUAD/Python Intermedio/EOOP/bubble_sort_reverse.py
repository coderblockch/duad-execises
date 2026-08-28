def bubble_sort_reverse(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1, 0, -1):        # recorre de derecha a izquierda
            if arr[j] < arr[j - 1]:           # si el actual es menor que su vecino izquierdo
                arr[j], arr[j - 1] = arr[j - 1], arr[j]   # swap
    return arr


numbers = [5, 2, 8, 1, 9, 3]
print("Before:", numbers)
print("After:", bubble_sort_reverse(numbers))