import math


def getThresholdFactors(n, threshold):
    """
    Factors a number with a threshold for factor size
    :param n: integer, the number to be factored
    :param threshold: integer, the threshold
    :return: a list of integers that are factors of n, strictly greater than threshold
    """
    small_factors = set()
    large_factors = set()
    for i in range(1, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            if i > threshold:
                small_factors.add(i)
            factor_pair = n // i
            large_factors.add(factor_pair)
    return small_factors.union(large_factors)


print(getThresholdFactors(64, 2))


def isConnectedDirectly(start_city, end_city, connections):
    """
    :param start_city:
    :param end_city:
    :param connections:
    :return: True if there is a direct connection between start_city and end_city
    """
    return end_city in start_city[connections]


def findPath(connections, threshold, start_city, end_city, visited ):
    """
    Determines the existance of a path between startCity and EndCity
    :param connections: the list of connections between individual cities
    :param threshold: the factoring threshold
    :param start_city: integer, the city to start
    :param end_city: integer, the city to end
    :param visited: list[int], the cities previously visited
    :return: 1 if a path exists, else 0
    """
    if threshold <= 1:
        return 1

    elif isConnectedDirectly(start_city, end_city, connections):
        return 1
    else:
        visited.append(start_city)
        for i in range(0, len(connections) + 1):
            if i not in visited:
                return findPath(connections, threshold, i, end_city, visited)
        return 0


def connectedCities(n, g, start_cities, end_cities):
    result = []
    connections = [getThresholdFactors(i, g) for i in range(1, n + 1)]
    connections.insert(0, [])  # inserts an entry for zero so list can be treated as 1-indexed for convenience
    print('connections', connections)
    for i in range(0, len(start_cities)):
        result.append(findPath(connections, g, start_cities[i], end_cities[i], []))
    print(result)

connectedCities(27, 2, [7,4,7,7,18], [10,8,14,10,12])
