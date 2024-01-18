import sys

def find(idx):
    if root[idx] == idx:
        return root[idx]
    root[idx] = find(root[idx])
    return root[idx]

n, m = map(int, input().split())
type = [0] + list(input().split())

edge = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edge.append((a, b, c))
    edge.append((b, a, c))

edge.sort(key = lambda x : x[2])
root = [i for i in range(n+1)]
answer, cnt = 0, 0
for a, b, c in edge:
    if type[a] != type[b]: # 남 -> 남, 여 -> 여 못감
        n1, n2 = find(a), find(b)
        if n1 != n2:
            root[n2] = n1
            answer += c
            cnt += 1
        
        if cnt == n-1: # 5개 node가 있다면 edge 4개만 있으면 다 연결가능
            print(answer)
            exit()
print(-1)