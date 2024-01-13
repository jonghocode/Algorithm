def find(x):
    if root[x] == x:
        return root[x]
    root[x] = find(root[x])
    return root[x]

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst = list(lst[1:])
party = []
root = [i for i in range(n+1)]
for _ in range(m):
    temp = list(map(int, input().split()))
    party.append(list(temp[1:]))

for i in range(len(party)):
    party[i].sort()
    for j in range(len(party[i])-1):
        a, b = find(party[i][j]), find(party[i][j+1])
        if a != b:
            if a in lst:
                root[b] = a
            elif b in lst:
                root[a] = b
            else:
                root[a] = b


for i in range(1, n+1):
    find(i)

answer = 0
for i in range(len(party)):
    sw = 0
    for j in range(len(party[i])):
        if root[party[i][j]] in lst:
            sw = 1
    if sw == 0:
        answer += 1

print(answer)