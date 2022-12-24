def get_max_activities(S):
    S = sorted(S, key=lambda x: x[1])
    max = []
    for i in range(len(S)):
        ans = [S[i]]
        count = i
        for j in range(len(S)):
            if S[count][1] <= S[j][0]:
                ans += [S[j]]
                count = j
        if len(ans) > len(max):
            max = ans

    return max
