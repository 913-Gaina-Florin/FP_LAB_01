# 1

def is_prime(n):
    """
    This function checks if a number is prime or not.
    :param n: natural number
    :return: true if the number is prime, false otherwise
    """
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_num_greater(n):
    """
    This function finds the first prime number greater than n and returns it.
    It does that by increasing the value of n until we find a prime number.
    :param n: natural number
    :return: the first prime number grater than n
    """
    while True:
        n = n + 1
        if is_prime(n):
            return n

