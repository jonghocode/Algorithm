# 생각은 했지만 인덱스를 컨트롤하기 어려워서 구현하지 못했음
def dfs(ll, lr, rl, rr):
    if ll > lr or rl > rr:
        return

    root = last[rr] # 후위순회의 루트가 답
    print(root, end=' ')
    leftsize = dict[root]-ll # 중위의 왼쪽부터 루트까지가 left
    rightsize = lr-dict[root] # 중위의 루트부터 오른쪽까지가 right
    dfs(ll, ll+leftsize-1, rl, rl+leftsize-1) # 왼쪽 중위 리스트 시작 끝, 후위 리스트 시작 끝
    dfs(lr-rightsize+1, lr,rr-rightsize, rr-1) # 오른쪽 중위 리스트 시작 끝, 후위 리스트 시작 끝

n = int(input())
dict = {}
mid = list(map(int, input().split()))
last = list(map(int, input().split()))
for i in range(n):
    dict[mid[i]] = i
print(dict)
dfs(0, n-1, 0, n-1)