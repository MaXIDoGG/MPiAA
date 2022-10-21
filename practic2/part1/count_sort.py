def counting_sort(arr):
    max = -999999
    min = 999999
    for i in range(len(arr)):
        if min > arr[i]:
            min = arr[i]
        if max < arr[i]:
            max = arr[i]
    counts = [0]*(max-min+1)
    for i in range(len(arr)):
        counts[arr[i] - min] += 1
    n = 0
    for i in range(len(counts)):
        for j in range(0, counts[i]):
            arr[n] = i + min
            n = n+1
    return arr
