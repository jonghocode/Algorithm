import operator

def solution(N, stages):
    answer = []
    f_dic = {}
    for i in range(1,N+1):
        n = 0
        f = 0
        for item in stages:
            if item >= i: n += 1
            if item == i: f += 1
        if n != 0:
            f_dic[i] = f/n
        else:
            f_dic[i] = 0
    f_dic = sorted(f_dic.items(), key=operator.itemgetter(1), reverse=True)

    for item in f_dic:
        answer.append(item[0])

    return answer