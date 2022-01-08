def checker(str):
    array = [str[0]]
    for i in range(1, len(str)):
        if str[i-1] != str[i]:
            array.append(str[i])

    #print(array)
    bool = True
    ans_array = []
    for i in range(len(array)):
        if (array[i] not in ans_array):
            ans_array.append(array[i])
        elif (array[i] in ans_array):
            bool = False
            break

    return bool

n = int(input())

result = 0
for i in range(n):
    if checker(input()):
        result += 1

print(result)
