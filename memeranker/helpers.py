from random import randint

def two_randint(max_val):

    if max_val<2:
        raise Exception(f"Maximum value {max_val} is too small to generate two random numbers")

    rand_int = randint(0, max_val - 1)
    rand_int2 = randint(0, max_val - 1)

    return two_randint(max_val) if rand_int2 == rand_int else [rand_int, rand_int2]
