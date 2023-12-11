from heapq import heappush, heappop
import sys

n = int(input())
promax = [] # 최대힙
promin = [] # 최소힙
sol = {}
lst = {}
for _ in range(n):
    p, l = map(int, sys.stdin.readline().split())
    heappush(promax, [-l, -p])
    heappush(promin, [l, p])
    lst[str(p)] = str(l) # 각 문제의 난이도를 저장

m = int(input())
for _ in range(m):
    command = list(sys.stdin.readline().strip().split())
    if command[0] == 'add': # 더하기
        lst[str(command[1])] = str(command[2]) # 각 문제의 난이도 저장
        heappush(promax, [-int(command[2]), -int(command[1])])
        heappush(promin, [int(command[2]), int(command[1])])

    elif command[0] == 'recommend': # 추천하기
        if command[1] == '1':
            while True: # sol안에 없는 것을 뽑을 때 까지 뽑기
                level, pro = -promax[0][0], -promax[0][1]
                level = str(level)
                pro = str(pro)
                if pro in sol: # 같은 문제 번호를 풀었다면
                    if level in sol[pro]: # 같은 문제 번호의 난이도가 있다면
                        heappop(promax) # 뽑기
                    else:
                        print(pro) # 중복되는 문제가 없기 때문에 출력
                        break
                else:
                    print(pro) # 중복되는 문제가 없기 때문에 출력
                    break
        
        
        elif command[1] == '-1':
            while True: # sol안에 없는 것을 뽑을 때 까지 뽑기
                level, pro = promin[0][0], promin[0][1]
                level = str(level)
                pro = str(pro)
                if pro in sol:
                    if level in sol[pro]:
                        heappop(promin)
                    else:
                        print(pro)
                        break
                else:
                    print(pro)
                    break

    elif command[0] == 'solved': # 풀었으면 sol에 넣기
        if command[1] not in sol:
            sol[command[1]] = []
        sol[command[1]].append(lst[command[1]])
        
    # print(f"promin : {promin}, solved : {sol}")

# 최소힙과 최대힙으로 난이도 낮은 문제와 높은 문제를 관리하고
# 추천을 받는것은 dictionary에 있지 않은 문제만 출력해준다.
# (추천을 받으면서 while문을 돌며 해당 문제가 sol에 있는문제라면 pop 해주고 아니라면 출력해준다.)
# 왜냐하면 매번 sol을 할 때 마다 del를 해주면 시간이 오래 걸리기 때문에
# dictionary에 넣어서 있는지 해당 문제번호가 풀렸는지 안풀렸는지 확인한다.
# 문제를 풀었다면 해당 문제마다 dict[문제번호] : [] 이렇게 리스트가 있기 때문에 append해준다.
# 왜 리스트를 넣냐하면 같은 문제 번호로 난이도가 다른게 또 들어올 수 있기 때문이다.