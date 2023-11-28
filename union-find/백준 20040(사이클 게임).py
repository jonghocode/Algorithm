# 백준 20040(사이클 게임)
# union-find 문제입니다. 연결된 노드 끼리 그룹으로 묶어서 연결 여부를 효율적으로
# 파악 가능합니다.
# 일반적인 bfs, dfs로 풀면 매번 탐색을 새로해야하기 때문에 매우 비효율적입니다.

import sys

def find(x): # 부모 노드 찾기
    if graph[x] == x: # 반환
        return x
    else: # 다르다면 부모노드 찾으러 가자
        graph[x] = find(graph[x]) # 재귀함수로(나중에 루트 노드 값이 들어옴)
        return graph[x]

def union(a, b): # 
    first = find(a)
    second = find(b)
    if first == second: # 부모 노드가 같다면 같은 집합
        return True
    
    if first > second: # 같은 집합이 아니라면 합치기(수가 작은 노드로 합쳐줌)
        graph[first] = second
    else:
        graph[second] = first

    return False

n, m = map(int, input().split())
graph = [i for i in range(n)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    
    if union(a, b):
        print(i+1)
        exit()

print(0)