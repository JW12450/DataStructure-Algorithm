n, k = map(int, input().split())

coin_list = []
for i in range(n):
    coin_list.append(int(input()))

coin_list.sort(reverse=True)

count = 0
for i in range(len(coin_list)):
    count += k//coin_list[i]
    k = k%coin_list[i]

print(count)