def get_max_activities(S):
    if S == []:
        return []
    min = 999999
    a = [[0, 0]]
    for i in range(len(S)):
        if (S[i][1]) < min:
            a[0] = S[i]
            min = S[i][1]
    C = []
    for i in range(len(S)):
        if (a[0][1] <= S[i][0]):
            C.append(S[i])
    return a + get_max_activities(C)

# def get_max_activities(S):
#     if S == []:
#         return []
#     a = [S[0]]
#     C = [[]]
#     for i in range(1, len(S)):
#         if(a[0][1] <= S[i][0]):
#             C = S[i:]
#             return a + get_max_activities2(C)
#     return a
