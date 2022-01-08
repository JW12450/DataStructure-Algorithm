mon, day = map(int, input().split())

mon_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

sum = 0
for i in range(mon-1):
    sum += mon_day[i]

sum += day-1

if (sum % 7 == 0):
    print('MON')
elif (sum % 7 == 1):
    print('TUE')
elif (sum % 7 == 2):
    print('WED')
elif (sum % 7 == 3):
    print('THU')
elif (sum % 7 == 4):
    print('FRI')
elif (sum % 7 == 5):
    print('SAT')
else :
    print('SUN')