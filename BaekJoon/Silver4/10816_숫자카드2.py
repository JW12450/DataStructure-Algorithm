import sys
from collections import Counter

# 가지고 있는 숫자 카드의 개수
n = int(sys.stdin.readline())

# 숫자 카드에 적혀 있는 정수들
num_list= list(map(int, sys.stdin.readline().split()))

# m 몇개 가지고 있는지 체크할 카드의 수
m = int(sys.stdin.readline())

check_list= list(map(int, sys.stdin.readline().split()))

count_dict = Counter(num_list)

for i in check_list:
    print(count_dict[i], end=" ")