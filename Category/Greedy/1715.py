"""
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array.sort()

count = array[0] + array[1]
count_list = [count]
save = 0
i = 2


while True:
    if (i == n-1):
        count += array[i]
        count_list.append(count)
        break
    elif (i == n-2):
        if count + array[i] > array[i] + array[i + 1]:
            count_list.append(array[i] + array[i + 1])
            count_list.append(count + array[i] + array[i + 1])
            #count += array[i] + array[i + 1]
            print('here')
            break
        else:
            count += array[i]
            count_list.append(count)
            # print(count_list)
            count += array[i + 1]
            count_list.append(count)
            # print(count_list)
            break
    elif count + array[i] > array[i] + array[i + 1]:
        count_list.append(array[i] + array[i + 1])
        count += array[i] + array[i + 1]
        count_list.append(count)
        i += 2
    else:
        count += array[i]
        count_list.append(count)
        # print(count_list)
        i += 1

#print(count_list)
print(sum(count_list))
"""

"""
while True:
    if (i == n-1):
        count += array[i]
        count_list.append(count)
        break
    elif (i == n-2):
        if count+array[i] > array[i] + array[i+1]:
            count_list.append(array[i] + array[i + 1])
            count += array[i] + array[i + 1]
            #print('here')
            break
        else:
            count += array[i]
            count_list.append(count)
            #print(count_list)
            count += array[i+1]
            count_list.append(count)
            #print(count_list)
            break

    elif count + array[i] > array[i] + array[i+1]:
        count_list.append(array[i] + array[i+1])
        count += array[i] + array[i+1]
        i += 2
    else:
        count += array[i]
        count_list.append(count)
        #print(count_list)
        i += 1

print(count_list)
print(sum(count_list))


1, 2, 3, 4, 5, 6 의 카드묶음이 있는 경우


1,2 = 3
3,3 = 6
6,4 = 10
10,5 = 15
15, 6 = 21

1,2 = 3
3,3 = 6
6,4 = 10
5, 6 = 11
10, 11 = 21


"""
import heapq # 우선순위 큐

N = int(input())

cardList = list(int(input()) for _ in range(N))
heapq.heapify(cardList)
result=0


while len(cardList) != 1:
    num1 = heapq.heappop(cardList)
    num2 = heapq.heappop(cardList)
    Sum = num1 + num2
    result += Sum
    heapq.heappush(cardList,Sum)

print(result)
