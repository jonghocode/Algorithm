a, b, c, d = map(int, input().split())

answer = 0
st = 0
for i in range(1, 25):
    if st + a <= d:
        st += a
        answer += b
    else:
        st -= c
        if st < 0:
            st = 0
    # print(f"i : {i}, st : {st}, answer : {answer}")
print(answer)