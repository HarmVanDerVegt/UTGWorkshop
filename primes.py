def find_primes(start: int, end: int):
    """
    This function finds prime numbers within the specified range [start, end].
    Parameters:
    start (int): The starting number of the range.
    end (int): The ending number of the range.
    Returns:
    list: A list of prime numbers within the specified range.
    """
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes