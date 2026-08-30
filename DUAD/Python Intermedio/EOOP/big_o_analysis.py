# ============================================
# Análisis de Algoritmos - Big O Notation
# ============================================


# --- Ejercicio 1: bubble_sort ---
# Big O: O(n²) - Cuadrático
# Razón: Tiene dos bucles anidados (for dentro de for), y cada uno
# recorre n elementos. En total n × n = n² operaciones. Por eso, con
# muchos datos, el bubble sort se vuelve lento.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# --- Ejercicio 2 ---

# print_numbers_times_2
# Big O: O(n) - Lineal
# Razón: Un solo bucle que recorre los n elementos de la lista una vez.
# El trabajo crece igual que la cantidad de datos.

def print_numbers_times_2(numbers_list):
    for number in numbers_list:
        print(number * 2)


# check_if_lists_have_an_equal
# Big O: O(n²) - Cuadrático
# Razón: Dos bucles anidados (uno por cada lista). Por cada elemento de
# list_a, recorre toda list_b. En total n × n = n² operaciones.

def check_if_lists_have_an_equal(list_a, list_b):
    for element_a in list_a:
        for element_b in list_b:
            if element_a == element_b:
                return True
    return False


# print_10_or_less_elements
# Big O: O(1) - Constante
# Razón: El bucle tiene un límite fijo por el min(list_len, 10): corre
# como máximo 10 veces, sin importar si la lista tiene 100 o 1 millón de
# elementos. El trabajo no crece con los datos, es constante.

def print_10_or_less_elements(list_to_print):
    list_len = len(list_to_print)
    for index in range(min(list_len, 10)):
        print(list_to_print[index])


# generate_list_trios
# Big O: O(n³) - Cúbico
# Razón: Tres bucles anidados (uno dentro de otro dentro de otro), cada
# uno recorre n elementos. En total n × n × n = n³ operaciones.

def generate_list_trios(list_a, list_b, list_c):
    result_list = []
    for element_a in list_a:
        for element_b in list_b:
            for element_c in list_c:
                result_list.append(f'{element_a} {element_b} {element_c}')
    return result_list