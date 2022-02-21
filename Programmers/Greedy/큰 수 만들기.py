import copy


def solution(number, k):
    answer = ''
    num = list(number)
    # print(num)
    # print("".join(map(str,num)))
    stack = []

    for i in range(len(number) - k):
        stack.append(num[i])
    # print(stack)

    for i in range(len(number) - k, len(number)):
        stack.append(num[i])
        comb = []
        for j in range(len(stack)):
            c = copy.deepcopy(stack)
            c.pop(j)
            comb.append(int("".join(map(str, c))))
        # print(comb)
        stack = list(str(max(comb)))
        # print(stack)

    return str("".join(stack))