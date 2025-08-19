import random

def random_nbit_int(n, rng=None):
    rng = rng or random
    return rng.randint(0, 2**n - 1)