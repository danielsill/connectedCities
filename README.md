# connectedCities
Tool used for finding paths between connected cities identified by integers

Problem description:

implement connectedCities(n, g, start_cities, end_cities)
    """
    Per the problem description, finds a path between each pair of start and end cities
    assumes len(start_cities) == len(end_cities) == len(return value)
    :param n: the number of cities in the map
    :param g: the threshold for factoring
    :param start_cities: list[int] starting cities
    :param end_cities: list[int] ending cities
    :return: a list denoting each end city is reachable from each start city with 1 as true
    """

A city is represented by an integer. The number of cities in the map are given by parameter n
Two cities are considered connected if they share a common factor greater than a certain threshold, given by g.
Determine if a path exists between each pair of cities represented by start_cities and end_cities.

i.e

n = 27
g = 2
start_cities = [7,4,18,7,7]
end_cities = [10,8,12,10,14]

returns: [0, 1, 1, 0, 1]

10 cannot be reached from 7 since 7 is prime it can only have a path to multiples of itself

8 can be reached from 4 directly because they share a factor greater than 2, which happens to be 4

12 can be reached from 18, first by traveling from 18 to 3, then 3 to 12

...etc.
