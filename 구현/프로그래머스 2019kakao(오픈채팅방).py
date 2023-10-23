def solution(record):
    answer = []
    dict = {}
    
    for word in record:
        line = word.split(' ')
        what, sid = line[0], line[1]
        if what == 'Enter':
            dict[sid] = line[2]
        elif what == 'Change':
            dict[sid] = line[2]

    for word in record:
        line = word.split(' ')
        what, sid = line[0], line[1]
        if what == 'Enter':
            answer.append(f"{dict[sid]}님이 들어왔습니다.")
        elif what == 'Leave':
            answer.append(f"{dict[sid]}님이 나갔습니다.")
    return answer