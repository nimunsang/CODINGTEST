def solution(numbers, target):

    answer = 0
    def dfs(n):
        nonlocal answer
        if sum(numbers) == target:
            answer += 1
            return

        for i in range(n, len(numbers)):
            numbers[i] = -1 * numbers[i]
            dfs(i+1)
            numbers[i] = -1 * numbers[i]


    dfs(0)
    return answer