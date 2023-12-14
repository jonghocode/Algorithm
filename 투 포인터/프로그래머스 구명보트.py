# 2개 합쳐서 무게제한이 있기 때문에 내림차순 정렬을 해준다.
# 두개 합쳐서 limit을 넘는다면 answer을 1올려주고 st도 올려준다.
# 넘지 않으면 둘 다 줄여준다.

def solution(people, limit):
    answer = 0
    st, ed = 0, len(people)-1
    people.sort(reverse = True)

    while st <= ed:
        if people[st] + people[ed] <= limit and st != ed:
            answer += 1; st += 1; ed -= 1
        elif people[st] + people[ed] > limit:
            st += 1; answer += 1
        else:
            answer += 1
            break

    return answer