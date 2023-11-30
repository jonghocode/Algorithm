def go(root):
    global before, mid, after
    if root == '.':
        return
    before += root
    go(graph[root][0][0])
    mid += root
    go(graph[root][0][1])
    after += root

n = int(input())
graph = {chr(i+65) : [] for i in range(n)}
for i in range(n):
    a, b, c = map(str, input().split())
    graph[a].append([b, c])

before, mid, after = '', '', ''
go('A')
print(before)
print(mid)
print(after)