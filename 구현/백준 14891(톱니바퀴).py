from collections import deque
def left(n,dir):
	if n >= 0 and lst[n][2] != lst[n+1][6]:
		left(n-1,-dir)
		lst[n].rotate(dir)

def right(n,dir):
	if n <= 3 and lst[n][6] != lst[n-1][2]:
		right(n+1,-dir)
		lst[n].rotate(dir)

lst = [deque(input()) for _ in range(4)]
k = int(input())
for _ in range(k):
	num,dir = map(int,input().split())
	num -= 1
	left(num-1,-dir)
	right(num+1,-dir)
	lst[num].rotate(dir)

ans = 0
for i in range(4):
	if lst[i][0] == '1':
		ans += 2**i
print(ans)