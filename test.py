def find(idx):
    if root[idx] == idx:
        return root[idx]
    root[idx] = find(root[idx])
    return root[idx]

n, m = map(int, input().split())
bad = list(map(int, input().split()))
bad = bad[1:]
party = []
for _ in range(m):
    temp = list(map(int, input().split()))
    party.append(temp[1:])

root = [i for i in range(n+1)]
for i in range(len(bad)-1):
    n1, n2 = find(bad[i]), find(bad[i+1])
    if n1 != n2:
        root[n2] = n1

for lst in party:
    for i in range(len(lst)-1):
        n1, n2 = find(lst[i]), find(lst[i+1])
        if n1 != n2:
            root[n2] = n1

answer = 0
n1 = find(bad[0])
for lst in party:
    n2 = find(lst[0])
    if n1 != n2:
        answer += 1

print(answer)