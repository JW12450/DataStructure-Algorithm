

import sys

n = int(sys.stdin.readline())

#단어의 개수 1~10 / 모든 단어에 알파벳은 최대 10개가 있고, 수의 최대 길이는 8
array = [] #단어 저장
dict = {} # 알파벳별로 수를 저장할 딕셔너리
num_list = [] #수를 저장할 리스트

for i in range(n):
    array.append(sys.stdin.readline().rstrip())

for i in range(n):
    for j in range(len(array[i])):
        if array[i][j] in dict:
            dict[array[i][j]] += 10 ** (len(array[i])-j-1)
        else:
            dict[array[i][j]] = 10 ** (len(array[i]) - j - 1)

for x in dict.values():
    num_list.append(x)

num_list.sort(reverse=True)

sum = 0
pows = 9
for i in num_list: # 첫 번째 부터 가장 큰 부분을 차지하므로 9를 곱해준다
    sum += pows * i
    pows -= 1
# 내려갈수록 그 알파벳이 차지하는 비중이 적으므로 -1
print(sum)
