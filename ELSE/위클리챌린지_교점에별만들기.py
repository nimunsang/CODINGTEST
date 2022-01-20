def solution(line):
    inf = float('inf')
    res = []
    L = len(line)
    x_min, y_min, x_max, y_max = inf, inf, -inf, -inf
    for i in range(L):
        for j in range(i, L):
            if i == j:
                continue
            A, B, E, C, D, F = [*line[i], *line[j]]
            Q = A*D-B*C
            if Q == 0:
                continue

            x = (B*F-E*D) / Q
            y = (E*C-A*F) / Q
            if int(x) != x or int(y) != y:
                continue

            x = int(x) 
            y = int(y)
            res.append((y, x))
            x_min = min(x, x_min)
            y_min = min(y, y_min)
            x_max = max(x, x_max)
            y_max = max(y, y_max)

    arr = [['.']*(x_max-x_min+1) for _ in range(y_max-y_min+1)]
    for y, x in res:
        arr[y_max - y][x - x_min] = '*'

    return [''.join(s) for s in arr]