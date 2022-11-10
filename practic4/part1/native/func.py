def nativeLcs(a, b):
    max = ''
    c = ''
    for i in range(len(a)):
        if a[i] in b:
            c += a[i]

    for k in range(len(c)):
        count = 0
        str1 = ''
        for i in range(k, len(c)):
            if count == len(b):
                break
            for j in range(count, len(b)):
                if c[i] == b[j]:
                    str1 += c[i]
                    count = j+1
                    break
        if len(str1) > len(max):
            max = str1
    return max
