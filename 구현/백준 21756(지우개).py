#(A) 홀수번 칸의 수들을 모두 지운다 (B) 남은 수들을 왼쪽으로 모은다.
n = int(input())
lst = [i for i in range(1, n+1)]

while True:
    if len(lst) == 1:
        print(lst[0])
        break
    if len(lst)%2 == 0:
        t = len(lst)//2
    else:
        t = len(lst)//2 + 1
    for i in range(t):
        lst.pop(i)
    