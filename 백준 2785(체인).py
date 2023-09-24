# 예제 3번을 이해 하지 못해서 어떤 접근 인지 보고 구현은 내가 했음
# 고리를 떼 와서 새로운 2개를 연결하는 것이었음! 고리를 떼오는 것은 생각하지 못했다.

n = int(input())
lst = list(map(int, input().split()))
answer = 0
lst.sort()
while len(lst) > 1:
    if lst[0] >= 1:
        lst[0] -= 1
        answer += 1
        lst.append(lst.pop() + lst.pop())
    else:
        lst.pop(0)
        continue
print(answer)
