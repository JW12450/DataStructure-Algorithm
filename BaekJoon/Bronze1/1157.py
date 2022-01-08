from string import ascii_lowercase

word = input().lower()
alphabet_list = list(ascii_lowercase)

alphabet_dict = {}
for i in range(len(alphabet_list)):
    alphabet_dict[alphabet_list[i]] = word.count(alphabet_list[i])

#print(alphabet_dict.keys())
#print(alphabet_dict.values())

max_val = max(alphabet_dict.values())
#print(max_val)

alp_list = list(alphabet_dict.keys())
count_list = list(alphabet_dict.values())
#print(count_list.count(max_val))

if (count_list.count(max_val) != 1):
    print('?')
else:
    max_index = count_list.index(max_val)
    print(alphabet_list[max_index].upper())