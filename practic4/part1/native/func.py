def nativeLcs(a, b):
    max = ''
    for k in range(len(a)):
        count = 0
        str1 = ''
        for i in range(k, len(a)):
            if count == len(b):
                break
            for j in range(count, len(b)):
                if a[i] == b[j]:
                    str1 += a[i]
                    count = j+1
                    break
        if len(str1) > len(max):
            max = str1
    return max
