sen = input()

a = list(sen.split("0"))
b = list(sen.split("1"))

#print(sen.split("0"))
#print(b)

for i in range(a.count('')):
    a.remove('')
for i in range(b.count('')):
    b.remove('')

# 0을 기준으로 나눈 리스트의 길이가 1을 기준으로 나눈 리스트의 길이보다 더 긴 경우 : 0들을 뒤집어야 함!
if (len(a) > len(b)):
    print(len(b))
else:
    print((len(a)))


#print(a.count(''))
#print(a)

