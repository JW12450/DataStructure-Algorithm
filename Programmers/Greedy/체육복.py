def solution(n, lost, reserve):
    re_l = []
    for r in reserve:
        if r in lost:
            re_l.append(r)

    for r in re_l:
        lost.remove(r)
        reserve.remove(r)

    lost.sort()
    reserve.sort()
    answer = n - len(lost)

    print(lost)
    print(reserve)

    for r in reserve:
        if r - 1 in lost:
            lost.remove(r - 1)
            answer += 1
        elif r + 1 in lost:
            lost.remove(r + 1)
            answer += 1

    return answer