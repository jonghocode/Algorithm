# 백준 14621(나만 안되는 연애) -> 최소 스패팅 트리(크루스칼) 은 아닌거같고,, 다익스트라 인듯 ,, -> 문제를 잘못읽었다 -> 최소 스패닝 트리 맞네(남 -> 남으로는 못감)
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
    if type[a] != type[b]:
        n1, n2 = find(a), find(b)
        if n1 != n2:
            root[n2] = n1
            answer += c
            cnt += 1
        
        if cnt == n-1:
            print(answer)
            exit()
print(-1)