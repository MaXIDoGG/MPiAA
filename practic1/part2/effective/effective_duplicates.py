from collections import Counter


def has_duplicates(arr):
    sortedArr = sorted(arr)
    for i in range(len(sortedArr)-1):
        if sortedArr[i] == sortedArr[i+1]:
            return True
    return False


def get_duplicates(arr):
    return [k for k, v in Counter(arr).items() if v > 1]
