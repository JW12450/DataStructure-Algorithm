def solution(numbers):
    answer = ''
    num_l = []
    for n in numbers:
        num_l.append(list(map(int, str(n))))
    num_l.sort(reverse=True, key=lambda x: x * 3)
    # print(num_l)

    for l in num_l:
        answer += ("".join(map(str, l)))

    if answer == "0" * len(numbers):
        answer = "0"
    return answer