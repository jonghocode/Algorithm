# 상, 하, 좌, 우 이동
# 안전지대 반복 종료
# 우산있으면 우산 들기, 가지고있는 우산 버리고 새로운 우산
# 우산 -1 or 체력 -1
# 우산 0 되면 사라짐 or 체력 0 되면 죽음
# 체력이 남아있으면 반복

n, h, d = map(int, input().split())
board = [list(input()) for _ in range((n))]
print(board)