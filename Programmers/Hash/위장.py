from itertools import combinations


def solution(clothes):
    answer = 0
    comb = {}
    for c in clothes:
        comb[c[1]] = 0
    for c in clothes:
        comb[c[1]] += 1

    array = []
    for c in comb:
        array.append(comb[c])
    # print(array)

    s = 1
    for a in array:
        s *= (a + 1)
    answer = s - 1

    """
    for i in range(1,len(array)+1):
        tmp = (list(combinations(array,i)))
        #print(tmp)
        for t in tmp:
            #print(t)
            if len(t) == 1:
                answer += t[0]
            else:
                save = 1
                for a in t:
                    #print(a)
                    save *= a
                answer += save

    """

    return answer