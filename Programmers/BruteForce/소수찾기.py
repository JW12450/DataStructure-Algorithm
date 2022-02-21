from itertools import permutations


def is_prime_num(n):
    for i in range(2, n):  # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False

    return True


def solution(numbers):
    answer = 0

    num = list(numbers)
    # print(num)
    comb = []
    for i in range(1, len(num) + 1):
        comb += list(permutations(num, i))
    # print(comb)

    cand = ["".join(c) for c in comb]

    # print(comb)
    cand = [c.lstrip('0') for c in cand]

    for i, c in enumerate(cand):
        if c == '':
            cand.pop(i)

    # print(cand)

    final_cand = list(set(cand))
    if '' in final_cand:
        final_cand.remove('')
    if '1' in final_cand:
        final_cand.remove('1')
    # print(final_cand)

    cnt = 0
    for f in final_cand:
        if is_prime_num(int(f)):
            cnt += 1

    return cnt