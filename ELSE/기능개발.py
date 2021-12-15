def solution(progresses, speeds):
    day = []
    for z in zip(progresses, speeds):
        if (100 - z[0]) // z[1] == (100 - z[0]) / z[1]:
            day.append((100-z[0]) // z[1])
        else:
            day.append((100-z[0]) // z[1] + 1)

    answer = []
    cnt = 1
    m = day[0]
    for i in range(len(day)):
        if i+1 == len(day):
            answer.append(cnt)
            break

        if day[i+1] > m:
            answer.append(cnt)
            cnt = 1
            m = day[i+1]
        else:
            cnt += 1
    return answer