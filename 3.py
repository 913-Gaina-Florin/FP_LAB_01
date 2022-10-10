# 13

def list_of_primes(n):
    """
    This function computes all the prime factors of a given number n and returns them via a list.
    :param n: natural number
    :return: list containing all the prime factors of a given number
    """
    res = []
    d = 2
    while n > 1 and d * d <= n:
        k = 0
        while n % d == 0:
            k = k + 1
            n = n // d

        if k:
            res.append(d)

        if d * d <= n:
            d = d + 1

    if n > 1 or len(res) == 0:  # leftover number > 1, means that number is prime; len(res) handles the case n = 1
        res.append(n)
    return res


def n_th_element(n):
    """
    This function finds the n-th element of the sequence using the function list_of_primes() defined above.
    :param n: natural number
    :return: the n-th element of the sequence
    """
    number = 1
    while n > len(list_of_primes(number)):
        n = n - len(list_of_primes(number))
        number = number + 1

    arr = list_of_primes(number)
    return arr[n-1]


