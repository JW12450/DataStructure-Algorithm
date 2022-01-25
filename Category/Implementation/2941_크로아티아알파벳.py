sen = input()

alp_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
count = 0
i = 0

while i < len(sen):
    cand1 = sen[i:i+2]
    cand2 = sen[i:i+3]

    if cand1 in alp_list:
        count +=1
        i +=2
    elif cand2 in alp_list:
        count +=1
        i +=3
    else:
        count+=1
        i += 1

print(count)