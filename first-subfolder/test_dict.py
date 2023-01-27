"""Преобразование строки в словарь """
"""str_1 = 'вологда=город house=дом True=1 5=отлично 9=божественно'"""
"""str_1 может быть сразу input()"""
"""  d = dict([tmp.split('=') for tmp in str_1.split()])  """


str_1 = "+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890"
lst_1 = list(str_1.split())
# lst_1.sort()

set_1 = set([tmp[0:2] for tmp in lst_1])
d = {}
temp_lst = []
for tmp in set_1:
    d[tmp] = temp_lst

for t_str in lst_1:

    if t_str[0:2] in d:
        a = t_str[0:2]
        d[a] = d.get(a, [])+[t_str]


# str = str_1.split(" ")
# d = {}
# for x in str:
#     key = x[0:2]
#     if key not in d.keys():
#         d[key] = [x]
#     else:
#         d[key] += [x]


print(*sorted(d.items()))
# for tmp in str_1.split():


# print(lst_1)
# d = dict([k=tmp[0:2] v=tmp[1:] for tmp in str_1.split()])
# print(*sorted(d.items()))


# import sys

# lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = ['5=отлично', '4=хорошо', '3=удовлетворительно']
# list_tmp = []
# for sub_str in lst_in:
#     new_list = sub_str.split('=')
#     list_tmp.append(new_list)
# lst_1 = []
# lst_2 = []
# for lst in list_tmp:
#     lst_1.append(int(lst[0]))
#     lst_2.append(lst[1])
# # d = dict(zip(lst_1, lst_2))
# d = {}
# i = 0
# for tmp_d in lst_1:
#     d[tmp_d] = lst_2[i]
#     i += 1
# print(*sorted(d.items()))

# lst_in = ['5=отлично', '4=хорошо', '3=удовлетворительно']
# d = {}
# for tmp in lst_in:
#     key, value = tmp.split('=')
#     print(key, value)
#     d[int(key)] = value


# print(*sorted(d.items()))

# str_1 = input()
# str_1 = 'вологда=город house=дом True=1 5=отлично 9=божественно'
# list_1 = str_1.split()
# list_2 = []
# for sub_str in list_1:
#     new_list = sub_str.split('=')
#     list_2.append(new_list)
# d = dict(list_2)
# if 'house' in d and 'True' in d and '5' in d:
#     print('ДА')
# else:
#     print('НЕТ')


# str_1 = input()
# list_1 = str_1.split()
# list_2 = []
# for sub_str in list_1:
#     new_list = sub_str.split('=')
#     list_2.append(new_list)
# dict_1 = dict(list_2)
# for key in dict_1:
#     dict_1[key] = int(dict_1[key])
# print(*sorted(dict_1.items()))


# my_dict = {}

# key_1 = input('''Please complete the dictionary.
# Enter the first key: ''')
# value_1 = input('Enter the first value: ')
# my_dict[key_1] = value_1

# key_2 = input('Enter the second key: ')
# value_2 = input('Enter the second value: ')
# my_dict[key_2] = value_2

# key_3 = input('Enter the third key: ')
# value_3 = input('Enter the third value: ')
# my_dict[key_3] = int(value_3)


# print(my_dict)

# my_dict = {'brand': 'Nissan', 'model': 'Teana', 'engin': 'gasolin'}

# del my_dict['brand']


# print(my_dict)
