n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
answer = []

def dfs(idx, d):
    if d == m:
        for i in range(d):
            print(answer[i], end = ' ')
        print()
        return
    
    for i in range(idx, n):
        answer.append(lst[i])
        dfs(i ,d+1)
        answer.pop(-1)

dfs(0, 0)