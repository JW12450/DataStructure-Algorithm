n = int(input())

money = [500, 100, 50, 10, 5, 1]

remain = 1000 - n

count = 0
for i in range(len(money)):
    count += remain//money[i]
    remain = remain % money[i]
    if (remain%money[i]) == 0:
        break


print(count)