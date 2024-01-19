# 4195 친구 네트워크(리스트가 아닌 딕셔너리를 이용한 union-find)
# 처음에 문제를 풀 때 리스트를 이용해서 문제를 풀었는데 좀 복잡했다.
# 그래서 다른 사람의 풀이를 봤는데 나랑 풀이는 비슷하지만 딕셔너리를 사용해서 풀었다.
# 딕셔너리에 key와 value를 사람 이름으로 해두고 그걸로 union find 알고리즘을 사용했다.
# 딕셔너리로 푸니까 바로 풀렸다. 앞으로 union find문제를 풀 때 dictionary를 사용해봐야겠다.

import sys

def find(idx):
    if root[idx] == idx:
        return root[idx]
    root[idx] = find(root[idx])
    return root[idx]

t = int(input())
for _ in range(t):
    n = int(input())
    root = {} # 최대로 나올 수 있는 경우의 수
    answer = {}
    for _ in range(n):
        a, b = map(str, sys.stdin.readline().strip().split())
        if a not in root:
            root[a] = a
            answer[a] = 1
        if b not in root:
            root[b] = b
            answer[b] = 1
        n1, n2 = find(a), find(b)
        
        if n1 != n2:
            root[n2] = n1
            answer[n1] += answer[n2]
                    
        print(answer[n1])