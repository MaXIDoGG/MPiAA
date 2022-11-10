def fillDynMatrix(a, b):
    Matrix = [0]*(len(a) + 1)
    for i in range(len(Matrix)):
        Matrix[i] = [0]*(len(b) + 1)
    for i, elA in enumerate(a):
        for j, elB in enumerate(b):
            if elA == elB:
                Matrix[i][j] = Matrix[i - 1][j - 1] + 1
            else:
                Matrix[i][j] = max(Matrix[i][j-1], Matrix[i - 1][j])
    return Matrix


def LCS_DYN(a, b):
    Matrix = fillDynMatrix(a, b)
    LCS = ''
    i = len(a) - 1
    j = len(b) - 1
    while i >= 0 and j >= 0:
        if a[i] == b[j]:
            LCS += a[i]
            i -= 1
            j -= 1
        elif Matrix[i-1][j] > Matrix[i][j-1]:
            i -= 1
        else:
            j -= 1

    LCS = LCS[::-1]
    return LCS
