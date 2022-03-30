n = int(input())

array = list(map(int, input().split()))
def check(array):
    for a in array:
        if a != 0:
            return False
    return True

def is_even(array):
    for a in array:
        if a %2 != 0:
            return False
    return True

def max_odd_index(array):
    max = 0
    max_index = 0
    for i, a in enumerate(array):
        if a %2 == 1 and a > max:
            max = a
            max_index = i
    return max_index

cnt = 0
while not check(array):
    #print(array)
    #모두 짝수인 경우에는 나누기 2
    if is_even(array):
        for i in range(len(array)):
            array[i] /= 2
        cnt += 1
    # 하나라도 짝수가 아닌 경우에는 홀수중에서 가장 큰 값 -1
    else:
        i = max_odd_index(array)
        array[i] -= 1
        cnt += 1

print(cnt)







"""
1 0
1 1
2 1



1 0 0
0 1 0
0 0 1
1 1 1
2 2 2
4 4 4
8 8 8
16 16 16


1
2
3
6
12
24
25
50
100


"""