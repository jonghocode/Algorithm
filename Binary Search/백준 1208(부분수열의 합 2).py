# 입력받는 배열의 길이가 40이기때문에 이때의 시간복잡도는 2^40이라서
# 시간초과가 난다. 그래서 배열을 반틈으로 나누고 구한다면 2^20 + 2^20 이므로 시간안에 들어올 수 있다.
n, s = map(int, input().split())
lst = list(map(int, input().split()))
answer = 0

dict = {}

def dfs(idx, end, sum, what):
    global s, n, answer
    if idx == end:
        if what == 'L': # 왼쪽 부분이라면
            if not sum in dict:
                dict[sum] = 1
            else:
                dict[sum] += 1
        elif s-sum in dict: # 오른쪽 부분이라면
            answer += dict[s-sum]
        return
    dfs(idx+1, end, sum+lst[idx], what)
    dfs(idx+1, end, sum, what)
    
dfs(0, n//2, 0, 'L')
dfs(n//2, n, 0, 'R')
if s == 0: # 아무것도 안 고르는 경우 있을 수 있기 때문
    answer -= 1

print(answer)