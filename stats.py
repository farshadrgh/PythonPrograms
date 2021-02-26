class Stats():

    def __init__(self):
        pass

    def average(lst):
        return __class__.sum(lst) / __class__.length(lst)

    def meanDeviation(lst):
        average = __class__.average(lst)
        mean_deviation = 0
        for v in lst:
            mean_deviation += abs(average - v)
        return mean_deviation / __class__.length(lst)

    def count(lst, value):
        return lst.count(value)


    def variance(lst):
        average = __class__.average(lst)
        variance = 0
        for v in lst:
            variance += ((average - v) ** 2)
        return variance / __class__.length(lst)

    def standardDeviation(lst):
        return __class__.variance(lst) ** 0.5

    def median(lst):
        lst = __class__.sort(lst)
        length = __class__.length(lst)
        mid = int(length / 2)

        if length % 2 == 0:
            return (lst[mid] + lst[mid - 1]) / 2
        return lst[mid]

    def max(lst):
        return max(lst)

    def min(lst):
        return min(lst)

    def range(lst):
        return __class__.max(lst) - __class__.min(lst)

    def sum(lst):
        return sum(lst)

    def length(lst):
        return len(lst)

    def sort(lst):
        return sorted(lst)

