n = int(input())

word_list = [[" " for _ in range(10)] for _ in range(n)]

for i in range(n):
    word_list[i] = list(input())

print(word_list)