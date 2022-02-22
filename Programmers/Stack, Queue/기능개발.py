def solution(progresses, speeds):
    answer = []

    day = []
    for i in range(len(speeds)):
        if (100 - progresses[i]) % speeds[i] == 0:
            day.append((100 - progresses[i]) // speeds[i])
        else:
            day.append((100 - progresses[i]) // speeds[i] + 1)

    # print(day)

    time = []  # 한번 배포될때 같이 개발될 수 있는 기능들의 리스트

    for d in day:
        if len(time) == 0:
            time.append(d)
        else:
            if time[0] >= d:
                time.append(d)
            else:
                answer.append(len(time))
                time = []
                time.append(d)
    answer.append(len(time))

    return answer