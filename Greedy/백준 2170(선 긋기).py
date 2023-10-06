import sys

n = int(input())
answer = 0
line = []
for i in range(n):
    line.append(list(map(int, sys.stdin.readline().strip().split())))

line.sort(key = lambda x : (x[0], x[1])) # 시작 점을 기준으로 오름차순 이 코드랑 그냥 sort랑 똑같음 ㅋㅋ
st, ed = line[0][0], line[0][1] # 시작값 초기화
# print(line)

for i in range(1, n):
    if ed < line[i][0]: # 시작 값이 그 전 값보다 크다면 그 전까지의 길이를 더해야함
        answer += ed - st
        st = line[i][0] # 기준 바꾸기
        ed = line[i][1]
    else: # 아니라면 선을 계속 늘려가야 되므로 ed값 바꿔주기
        if ed < line[i][1]: # 이 if문은 내 스스로 만든 반례를 넣다가 찾아냈음
            ed = line[i][1] # 더 큰 값 넣기(작아지면 안됨)
    # print(f"i : {i}, st : {st}, ed : {ed}, answer : {answer}")

answer += ed - st # 반복문을 나오고 나서도 더해줘야함 -> 항상 그 전까지의 길이를 더해줬기 때문
print(answer)
