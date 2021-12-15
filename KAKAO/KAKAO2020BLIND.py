def solution(s):
    mask = 1
    minimum = 1000
    if len(s) == 1: return 1
    while mask < len(s):
        ans = ""
        start = 0
        cnt = 1
        while start < len(s):
            if s[start:start+mask] == s[start+mask:start+2*mask]:
                cnt += 1
                start += mask

            else:
                if cnt == 1:
                    ans += s[start:start+mask]
                    start += mask
                else:
                    ans += str(cnt) + s[start:start+mask]
                    start += mask
                    cnt = 1
        if len(ans) < minimum:
            minimum = len(ans)
        mask += 1
        
    return minimum