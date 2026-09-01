def sum_list(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total


# Prueba
print(sum_list([4, 6, 2, 29]))    # debe dar 41