
"""

def check30(word):
    if '0' not in word:
        return -1
    else:
        array = [0 for i in range(len(word))]
        for i in range(len(word)):
            array[i] = int(word[i])

        check =sum(array)
        if check%3 != 0:
            return -1
        else:
            array.sort()
            result = 0
            for i in range(len(array)):
                result += array[i] * (10 ** i)
            return result


word = input()
print(check30(word))
"""



n = list(input())
n.sort(reverse=True)
sum = 0
for i in n:
    sum += int(i)
if sum % 3 != 0 or "0" not in n:
    print(-1)
else:
    print(''.join(n))