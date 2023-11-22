def twoNumberSum(array, targetSum):
    for iFirst, first in enumerate(array):
        for iSecond, second in enumerate(array):
            if iFirst == iSecond:
                continue
            if (first + second) == targetSum:
                return [first, second]
    return []
