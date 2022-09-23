def has_duplicates(arr):
    for elem in arr:
        i = 0
        for elem1 in arr:
            if elem == elem1:
                i += 1
            if i > 1:
                return True
    return False


def get_duplicates(arr):
    arr1 = []
    for elem in arr:
        if elem in arr1:
            continue
        i = 0
        for elem1 in arr:
            if elem == elem1:
                i += 1
            if i > 1:
                arr1.append(elem)
                break

    return arr1
