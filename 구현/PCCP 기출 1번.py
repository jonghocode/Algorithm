# t초 동안 붕대감기, 1초 x 회복, t초 연속 붕대 y 추가 상승
# 최대 체력
# 공격당하면 기출 취소, 체력회복 x, 체력 깎임(현재체력 0 이하 캐릭터 죽음)
# 기술취소 당하거나 기술 끝나면 붕대감기 연속성공시간0 초기화
# 캐릭터가 생존할 수 있는지
# 시전시간, 초당 회복량, 추가 회복량
# 공격시간, 피해량

def solution(bandage, health, attacks):
    answer = 0
    end = attacks[-1][0]
    MAX = health
    success = 0
    idx = 0
    
    for time in range(1, end+1):
        if health <= 0:
            answer = -1
            break
        if attacks[idx][0] == time: # 공격시간이라면
            success = 0
            health -= attacks[idx][1]
            idx += 1
        else:
            success += 1
            add = bandage[1]
            if success == bandage[0]: # 추가회복
                add += bandage[2]
                success = 0
            if health + add < MAX:
                health += add
            else:
                health = MAX
    
    if health <= 0:
        answer = -1
    if answer != -1:
        answer = health
    return answer
