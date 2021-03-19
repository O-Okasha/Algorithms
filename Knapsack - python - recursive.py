# Knapsack problem - recursive
from timeit import default_timer as timer

weight = [3, 1, 3, 4, 2]  # weight of the items
value = [2, 2, 4, 5, 3]  # Value of the items


def knapsack(C, W, V):
    cache = [[0] * (C + 1) for y in range(len(W) + 1)]
    start = timer()
    answer = knapsack_cached(C, W, V, cache)
    end = timer()
    print(end - start)
    return answer


def knapsack_cached(C, W, V, cache):
    """
    This function calculates the highest value possible for the items in respect to their weights and maximum capacity.
    :param cache: (List)(list of ints) Table used to cache repeated answers
    :param C: (int) Maximum capacity of the knapsack.
    :param W: (list) list of all item weights.
    :param V: (list) list of all item values (Same index).
    :return: (list) containing list of tuples with all picked items and maximum value.
    """
    # Base cases
    if C == 0 or len(W) == 0:
        return 0
    if cache[len(W)][C] != 0:
        return cache[len(W)][C]
    _weight = W[0]
    _value = V[0]
    if _weight > C:
        cache[len(W)][C] = knapsack_cached(C, W[1:], V[1:], cache)
        return cache[len(W)][C]

    max_cache = max(knapsack_cached(C, W[1:], V[1:], cache), knapsack_cached(C - _weight, W[1:], V[1:], cache) + _value)
    cache[len(W)][C] = max_cache

    return cache[len(W)][C]


print(knapsack(7, weight, value))