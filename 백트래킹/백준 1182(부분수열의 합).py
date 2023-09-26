def dfs(d, sum, hit):
    global answer, n, s
    if d == n:
        if hit >= 1 and s == sum:
            answer += 1
        return
    dfs(d+1, sum, hit)
    dfs(d+1, sum+lst[d], hit+1)

answer = 0
n, s = map(int, input().split())
lst = list(map(int, input().split()))

dfs(0, 0, 0)
print(answer)