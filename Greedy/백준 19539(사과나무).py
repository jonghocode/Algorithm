n = int(input())
tree = list(map(int, input().split()))
s = sum(tree)
if s % 3 == 0:
    cnt = 0
    for i in tree:
        if i%2 == 1: # 2를 못 쓰는 개수
            cnt+=1
    # s//3은 총 횟수
    if cnt <= s//3:
        print("YES")
    else:
        print("NO")
else:
    print("NO")