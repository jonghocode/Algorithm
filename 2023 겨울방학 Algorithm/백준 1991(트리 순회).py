def Print(answer):
    for i in range(n):
        print(answer[i], end='')
    print()
def dfs(root):
    if root == '.':
        return
    answer1.append(root)
    dfs(graph[root][0][0])
    answer2.append(root)
    dfs(graph[root][0][1])
    answer3.append(root)

n = int(input())
graph = {chr(ord('A') + i) : [] for i in range(n)}
for i in range(n):
    k, l, r = map(str, input().split())
    graph[k].append((l, r))

answer1, answer2, answer3 = [], [], []
dfs('A')
Print(answer1)
Print(answer2)
Print(answer3)