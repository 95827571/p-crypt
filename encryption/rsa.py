# prime numbers
p, q = 5, 11

# finds number that is relatively prime
# - https://stackoverflow.com/questions/39678984/efficiently-check-if-two-numbers-are-co-primes-relatively-primes
# from here but modified
def gcd(a, b):
    if (b == 0):
        return abs(a)
    
    return gcd(b, a % b)


def prepare_rsa(p, q):

    # product of our two prime numbers
    N = p * q

    # the totient of n
    # the number of positive integers that are less than or equal to it and are coprime
    N0 = (p-1) * (q-1)

    # find the first integer that is relatively prime to our totient of n
    # it's not gonna be 1, and it's not gonna be N0
    for i in range(2, N0):
        if gcd(i, N0) == 1:
            encryption_exponent = 1
            break