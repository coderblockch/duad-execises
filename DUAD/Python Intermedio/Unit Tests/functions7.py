def is_prime(number):
    if number < 2:              # 0 y 1 no son primos
        return False
    for divisor in range(2, number):    # prueba del 2 al número anterior
        if number % divisor == 0:       # ¿divide exacto?
            return False                # tiene un divisor → NO es primo
    return True                         # ningún divisor → SÍ es primo

def get_primes(numbers):
    primes = []
    for number in numbers:
        if is_prime(number):        # usa la función de arriba
            primes.append(number)
    return primes


# Prueba
print(get_primes([1, 4, 6, 7, 13, 9, 67]))    # debe dar [7, 13, 67]