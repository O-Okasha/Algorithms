from timeit import default_timer as timer

R = 1
B = 2
cap = 100
c = [0 for i in range(cap+1)]


def tiling(C, cache):
    """
    This function calculates all the possible combinations of R and B in a size of C
    :param cache: (list of int) used to cache function calls
    :param C: (Int) Size of the area to be tiled
    :return: (Int) Number of all possible combinations
    """
    # If function call is cached, return cached value
    if cache[C] != 0:
        return cache[C]
    # If capacity is equal to or larger than 2, try adding R and B
    elif C >= B:
        cache[C] = tiling(C - B, cache) + tiling(C - R, cache)
        return cache[C]
    # If capacity is 1, add R
    elif C == R:
        cache[C] = tiling(C - R, cache)
        return cache[C]
    # If capacity is 0, return 1 as this is one complete combination
    elif C == 0:
        return 1


start = timer()
print(tiling(100, c))
end = timer()
print(end - start)
