# Sorting-String-Python
This Program sorts a string with 
- Lower-case letters before Upper-case letter 
- Upper-case Letters before Numerical digits 
- Numerical Digits before other Special characters



```
s = input()        # the alphanumeric string to be sorted

# defining empty lists to bifercate every index of the string respectively
strl_lst = []
stru_lst = []
num_lst = []
extra_lst = []

# iterate the string to every index
for i in s:
    if i.isalpha():     # check the character is alphabatic
        if i.islower(): # checks the alphabet is of lowercase
            strl_lst.append(i)
        else:           # if the alphabet is not lowercase then definitely it is uppercase
            stru_lst.append(i)
    elif i.isnumeric(): # checks if the char is numeric
        num_lst.append(int(i))
    else:               # if the char is neither alpha or numeric then definitely it is special char
        extra_lst.append(i)

# sorts every numeric value then maps the sorted list to str to convert in string then converts the mapped object to list
num = list(map(str, sorted(num_lst, key=lambda x: [not x % 2, x])))

# final sorted concatenated list
final_lst = sorted(strl_lst) + sorted(stru_lst) + num + sorted(extra_lst)

# join each element of the concatenated list and print it
print("".join(final_lst))
```
