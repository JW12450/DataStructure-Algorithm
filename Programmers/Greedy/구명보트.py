def solution(people, limit):
    cnt = 0

    people.sort(reverse=True)
    # print(people)

    start = 0
    end = len(people) - 1
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
            cnt += 1
        else:
            start += 1
            cnt += 1
    """
    while people:
        if len(people) == 1:
            cnt += 1
            break
        if people[0] + people[-1] <= limit:
            people.pop(0)
            people.pop()
            cnt += 1
        else:
            people.pop(0)
            cnt += 1
        #print(people)
    """
    return cnt