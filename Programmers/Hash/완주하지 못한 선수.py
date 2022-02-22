def solution(participant, completion):
    answer = ''
    dict = {}
    for p in participant:
        dict[p] = 0
    for p in participant:
        dict[p] += 1
    # print(dict)
    for c in completion:
        dict[c] -= 1
    for key, value in dict.items():
        if value > 0:
            answer = key
            break

    return answer

"""
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(answer.keys())
    return list(answer.keys())[0]
"""