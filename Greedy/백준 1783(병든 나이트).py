# n이 크면 위로가기
# m이 크면 오른쪽으로 가기
# 처음에 큰쪽으로 이동해보고 4번 이상이면 다른방법
n, m = map(int, input().split())

if n == 1:
    print(1)
elif n == 2:
    print(4, (m+1) // 2)
else:
    if m >= 7:
        print(m-2)
    else:
        print(min(4, m))