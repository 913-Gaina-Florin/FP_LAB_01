# 10

def palindrome(n):
    """
    This function computes and returns the palindrome of a given number.
    :param n: natural number
    :return: the palindrome of the given number
    """
    aux = 0
    while n:
        aux = aux * 10 + n % 10
        n = n // 10
    return aux
