def bubble_sort_reverse(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - 1, 0, -1):        # recorre de derecha a izquierda
            if lista[j] < lista[j - 1]:       # si el actual es menor que su vecino izquierdo
                lista[j], lista[j - 1] = lista[j - 1], lista[j]   # swap
    return lista


numbers = [5, 2, 8, 1, 9, 3]
print("Before:", numbers)
print("After:", bubble_sort_reverse(numbers))