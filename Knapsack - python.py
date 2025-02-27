# Knapsack problem

weight = [3, 1, 3, 4, 2]  # weight of the items
value = [2, 2, 4, 5, 3]  # Value of the items


def knapsack(C, W, V):
    """
    This function calculates the highest value possible for the items in respect to their weights and maximum capacity.
    :param C: (int) Maximum capacity of the knapsack.
    :param W: (list) list of all item weights.
    :param V: (list) list of all item values (Same index).
    :return: (list) containing list of tuples with all picked items and maximum value.
    """

    # Creating table where each row is value and each column is a specific capacity 0 -> C
    table = [[0]*(C+1) for y in range(len(W)+1)]
    numberOfItems = len(W)
    answer = [[]]

    # loop to solve the knapsack problem and fill the table
    for i in range(1, numberOfItems+1):
        _weight = W[i-1]  # Weight of current element
        _value = V[i-1]  # Value of current element

        for size in range(1, C+1):

            table[i][size] = table[i - 1][size]  # Same value as the row above it, as if it was not picked

            # Consider picking the item if there is enough weight for it
            # and it's value + the value of the item one row above and W behind it in capacity
            # is currently higher than the value of the item above it in the table
            if size >= _weight:
                if table[i - 1][size - _weight] + _value > table[i][size]:
                    table[i][size] = table[i - 1][size - _weight] + _value

    # will always be the best possible value
    answer.append(table[-1][-1])

    for i in range(numberOfItems, 1, -1):
        if table[i][C] != table[i - 1][C]:
            answer[0].append((W[i-1], V[i-1]))
            C -= W[i-1]

    return answer


print(knapsack(7, weight, value))
