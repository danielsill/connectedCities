import math


def getThresholdFactors(n, threshold):
    small_factors = []
    large_factors = []
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            if i >= threshold:
                small_factors.append(i)
            factor_pair = n//i
            if factor_pair != i:
                large_factors.append(factor_pair)
    return small_factors + large_factors[::-1]


print(getThresholdFactors(64, 2))