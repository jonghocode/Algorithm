def dfs(root, d):
    global answer
    if root == remove_node:
        return
    cnt = 0
    for i in tree[root]:
        if i != remove_node:
            dfs(i, d+1)
            cnt += 1
    if cnt == 0:
        answer += 1

n = int(input())
graph = list(map(int, input().split()))
tree = {i : [] for i in range(n)}
answer = 0
for i in range(n):
    if graph[i] == -1:
        root = i
    else:
        tree[graph[i]].append(i)

remove_node = int(input())
dfs(root, 0)
print(answer)