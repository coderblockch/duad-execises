# ============================================
# Algorithm Analysis - Big O Notation
# ============================================


# --- Exercise 1: bubble_sort ---
# Big O: O(n²) - Quadratic
# Reason: It has two nested loops (a for inside another for), and each
# one iterates over n elements. In total, n × n = n² operations. That is
# why, with large amounts of data, bubble sort becomes slow.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# --- Exercise 2 ---

# print_numbers_times_2
# Big O: O(n) - Linear
# Reason: A single loop that iterates over the n elements of the list
# once. The work grows at the same rate as the amount of data.

def print_numbers_times_2(numbers_list):
    for number in numbers_list:
        print(number * 2)


# check_if_lists_have_an_equal
# Big O: O(n²) - Quadratic
# Reason: Two nested loops (one for each list). For each element in
# list_a, it iterates over all of list_b. In total, n × n = n² operations.

def check_if_lists_have_an_equal(list_a, list_b):
    for element_a in list_a:
        for element_b in list_b:
            if element_a == element_b:
                return True
    return False


# print_10_or_less_elements
# Big O: O(1) - Constant
# Reason: The loop has a fixed limit due to min(list_len, 10): it runs at
# most 10 times, regardless of whether the list has 100 or 1 million
# elements. The work does not grow with the data, it stays constant.

def print_10_or_less_elements(list_to_print):
    list_len = len(list_to_print)
    for index in range(min(list_len, 10)):
        print(list_to_print[index])


# generate_list_trios
# Big O: O(n³) - Cubic
# Reason: Three nested loops (one inside another inside another), each
# one iterates over n elements. In total, n × n × n = n³ operations.

def generate_list_trios(list_a, list_b, list_c):
    result_list = []
    for element_a in list_a:
        for element_b in list_b:
            for element_c in list_c:
                result_list.append(f'{element_a} {element_b} {element_c}')
    return result_list