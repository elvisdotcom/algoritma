
# Sieve of Eratosthenes

def primes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for i, is_prime in enumerate(a):
        if is_prime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False
