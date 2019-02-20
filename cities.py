import math


def getThresholdFactors(n, threshold):
    """
    Factors a number with a threshold for factor size
    :param n: integer, the number to be factored
    :param threshold: integer, the threshold
    :return: a list of integers that are factors of n, strictly greater than threshold
    """
    small_factors = []
    large_factors = []
    for i in range(1, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            if i > threshold:
                small_factors.append(i)
            factor_pair = n//i
            if factor_pair != i:
                large_factors.append(factor_pair)
    return small_factors + large_factors[::-1]


print(getThresholdFactors(64, 2))