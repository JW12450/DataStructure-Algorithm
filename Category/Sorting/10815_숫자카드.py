import sys

n = int(sys.stdin.readline())
card_list = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
check_list = list(map(int, sys.stdin.readline().split()))

dict1 = {check_list[i]:0 for i in range(len(check_list))}

for i in range(n):
    if card_list[i] in dict1.keys():
        dict1[card_list[i]] += 1
print(" ".join(map(str, list(dict1.values()))))