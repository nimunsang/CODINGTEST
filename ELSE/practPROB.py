def solution(n):
    start = 0
    i = 1
    minimum = 0
    maximum = 0
    answer = []
    while True:
        if start < n <= start + 3**i:
            minimum = start+1
            maximum = start + 3**i
            break
        start = start + 3**i
        i += 1


    def find(a, b, n):
        if b-a <= 1:
            return

        if a <= n < a+(b-a+1)//3:
            answer.append(1)
            find(a, a+(b-a+1)//3, n)

        elif a+(b-a+1)//3 <= n < a+(b-a+1)*2//3:
            answer.append(2)
            find(a+(b-a+1)//3, a+(b-a+1)*2//3, n)

        elif a+(b-a+1)*2//3 <= n <= b:
            answer.append(4)
            find(a+(b-a+1)*2//3, b, n)


    find(minimum, maximum, n)
    return ''.join(map(str, answer))