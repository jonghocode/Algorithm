chk = [0]*10
answer = []

def search(n, m, d):
    if d == m:
        for i in range(m):
            print(answer[i], end=" ")
        print()
        return
    
    before = -1
    for i in range(n):
        if chk[i] == 0 and before != lst[i]:
            chk[i] = 1
            answer.append(lst[i])
            before = lst[i]
            search(n, m, d+1)
            answer.pop(-1)
            chk[i] = 0


n,m = map(int, input().split())
lst = list(map(int,input().split()))
lst.sort()

search(n, m, 0)