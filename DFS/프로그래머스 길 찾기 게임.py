# 처음에 문제를 풀 때 리스트로 왼쪽 오른쪽을 나누지 않고
# 바로바로 x,y값을 줘서 들어가게 만들었더니 9번에서 바로 5번으로 가는 것이었다.
# 그래서 이 방법으로는 안되겠다 싶어서 리스트로 왼쪽 오른쪽을 확실히 나눠서 풀었다.
import sys
sys.setrecursionlimit(10**6)
def solution(nodeinfo):
    def dfs(lst):
        parent = lst[0]
        left = []
        right = []
        
        # 리스트로 오른쪽 왼쪽을 확실히 나눠주기
        for i in range(1, len(lst)):
            if parent[0] < lst[i][0]: # 오른쪽
                right.append(lst[i])
            else: # 왼쪽
                left.append(lst[i])
        
        
        answer.append(parent[2]) # 전위 탐색이니까 먼저 답 넣어주기
        if left:
            dfs(left)
        if right:
            dfs(right)
        answer2.append(parent[2]) # 후위 탐색이니까 마지막에 답 넣어주기
        
    
    answer, answer2 = [], []
    answer3 = [answer, answer2]
    chk = [0 for _ in range(len(nodeinfo)+1)]
    
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    
    temp = sorted(nodeinfo, key = lambda x : (-x[1], x[0])) # 정렬
    dfs(temp)
    
    return answer3
