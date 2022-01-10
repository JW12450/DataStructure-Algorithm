n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array.sort()

count = array[0] + array[1]
count_list = [count]
i = 2
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
"""