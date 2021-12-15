def solution(lottos, win_nums):
    cnt = 0
    for num in lottos:
        if num in win_nums:
            cnt += 1
    
    cnt_0 = lottos.count(0)
    
    if cnt + cnt_0 <= 1:
        min_rank = max_rank = 6
    
    elif cnt <= 1:
        min_rank = 6
        if cnt_0 >= 1:
            max_rank = 7-(cnt+cnt_0)
            
    elif cnt > 1:
        min_rank = 7 - cnt
        max_rank = 7 - (cnt+cnt_0)
    
    answer = [max_rank, min_rank]
    return answer