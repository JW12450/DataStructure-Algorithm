def solution(array, commands):
    answer = []
    for c in commands:
        new = array[c[0] - 1:c[1]]
        new.sort(reverse=False)
        # print(new)

        answer.append(new[c[2] - 1])
        # print(new)
        # print(new[c[2]])
    return answer