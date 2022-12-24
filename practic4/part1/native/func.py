def nativeLcs(a, b, i, j, ans):
    if(i == len(a) or j == len(b)):
        return ans
    elif(a[i] == b[j]):
        ans += a[i]
        ans = nativeLcs(a, b, i+1, j+1, ans)
        return ans
    else:
        ans1 = nativeLcs(a, b, i+1, j, ans)
        ans2 = nativeLcs(a, b, i, j+1, ans)
        if(len(ans1) >= len(ans2)):
            ans = ans1
        else:
            ans = ans2
        return ans