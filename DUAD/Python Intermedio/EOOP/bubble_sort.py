def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


numbers = [5, 2, 8, 1, 9, 3]
print("Before:", numbers)
print("After:", bubble_sort(numbers))