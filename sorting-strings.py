s = input()
strl_lst = []
stru_lst = []
num_lst = []
extra_lst = []
for i in s:
    if i.isalpha():
        if i.islower():
            strl_lst.append(i)
        else:
            stru_lst.append(i)
    elif i.isnumeric():
        num_lst.append(int(i))
    else:
        extra_lst.append(i)

num = list(map(str, sorted(num_lst, key=lambda x: [not x % 2, x])))
final_lst = sorted(strl_lst) + sorted(stru_lst) + num + sorted(extra_lst)

print("".join(final_lst))