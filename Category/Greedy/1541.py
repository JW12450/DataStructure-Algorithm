array = list(map(str, input().split("-")))

def cal_plus(str):
    if ('+' in str):
        min_array = str.split("+")
        sum = int(min_array[0])
        for i in range(1,len(min_array)):
            sum += int(min_array[i])
        return sum
    else:
        return int(str)

result = cal_plus(array[0])
for i in range(1,len(array)):
    result -= cal_plus(array[i])

print(result)