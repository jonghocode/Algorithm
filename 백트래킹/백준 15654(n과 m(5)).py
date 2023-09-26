n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
answer = []
chk = [0]*10

def dfs(x, d):
    if d == m:
        for i in range(d):
            print(answer[i], end=' ')
        print()
        return


    for i in range(n):
        if chk[i] == 0:
            chk[i] = 1
            answer.append(lst[i])
            dfs(lst[i], d+1)
            answer.pop(-1)
            chk[i] = 0

dfs(0, 0)