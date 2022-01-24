array = list(map(int, input().split()))

array2 = array.copy()
array3 = array.copy()

array2.sort()
array3.sort(reverse=True)

if (array == array2):
    print("ascending")
elif (array == array3):
    print("descending")
else:
    print("mixed")
    