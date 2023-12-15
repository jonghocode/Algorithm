# 처음 두 분류를 묶어두고 2를 나눠주면서 구간을 나눈다.
# 두 구간이 똑같아진다면 같은 그룹으로 묶인것이다.
def solution(n,a,b):
    global answer
    answer = 0
    if a % 2 != 0:
        a = (a+1)
    if b % 2 != 0:
        b = (b+1)
    
    def p(x, y, d):
        global answer
        if x == y:
            answer = d+1
            return
        
        if x % 2 != 0:
            x = (x+1)
        if y % 2 != 0:
            y = (y+1)
        p(x//2, y//2, d+1)
    
    p(a//2, b//2, 0)
    
    return answer