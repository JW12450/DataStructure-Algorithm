def solution(phone_book):
    answer = True

    dict = {}
    for p in phone_book:
        dict[p] = 1

    for p in phone_book:
        for i in range(len(p)):
            if p[:i] in dict:
                answer = False
                break

    return answer