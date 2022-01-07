def solution(name):  
    answer =0
    ind = 0
    for i in range(len(name)):
        if name[i] != 'A':
            ind = i
               
    name2 = name[0]+ name[:0:-1]
    ind2 = 0
    for i in range(len(name2)):
        if name2[i] != 'A':
            ind2 = i
            
    if ind2 < ind:
        name = name2
        ind = ind2
            
    for i in range(len(name)):
        if i == ind+1:
            break
        answer += min(ord(name[i]) - ord('A'), 26-(ord(name[i]) - ord('A')))+1
    
    return answer-1