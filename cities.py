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
    intersection = connections[start_city].intersection(connections[end_city])
    return len(intersection) > 0


def findPath(connections, start_city, end_city, visited):
    """
    Determines the existance of a path between startCity and EndCity
    :param connections: the list of connections between individual cities
    :param start_city: integer, the city to start
    :param end_city: integer, the city to end
    :param visited: list[int], the cities previously visited
    :return: 1 if a path exists, else 0
    """
    if isConnectedDirectly(start_city, end_city, connections):
        return 1
    else:
        visited.append(start_city)
        for i in range(0, len(connections[start_city]) + 1):
            if i not in visited:
                return findPath(connections, i, end_city, visited)
        return 0


def connectedCities(n, g, start_cities, end_cities):
    """
    Per the problem description, finds a path between each pair of start and end cities
    assumes len(start_cities) == len(end_cities) == len(return value)
    :param n: the number of cities in the map
    :param g: the threshold for factoring
    :param start_cities: list[int] starting cities
    :param end_cities: list[int] ending cities
    :return: a list denoting each end city is reachable from each start city with 1 as true
    """
    if g <= 1:
        return 1 * len(start_cities)
    result = []
    connections = [getThresholdFactors(i, g) for i in range(1, n + 1)]
    connections.insert(0, set())  # inserts an entry for zero so list can be treated as 1-indexed for convenience
    print('connections', connections)
    for i in range(0, len(start_cities)):
        result.append(findPath(connections, start_cities[i], end_cities[i], []))
    print(result)
    return result

connectedCities(27, 2, [7,4,7,7,18], [10,8,14,10,12])
