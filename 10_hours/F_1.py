# # not or and
# my_list = [1, 4]

# my_list and print(f'List is note empty: {my_list }')

# print(bool(my_list and my_dict))
# my_dict['car'] = 'Teana'
# print(bool(my_list and my_dict))


# other_list = ['a', 'b']

# print(len(my_list) < 0 or other_list[0])


# Ложные значения
# print(bool(0))
# print(bool(0.0))
# print(bool(0j))
# print(bool(False))
# print(bool(None))
# print(bool({}))
# print(bool((1, 3)))
# print(bool(set()))
# print(bool(range(0)))
# print(bool(''))
# print(not not {1, 2})
# print(False or 0 or [1, 3, 5] or 435)
# print(234 and len([1]) and 435 and 24 and 45.5)


# Операторы
# my_dict = {
#     'brand': 'Nissan',
#     'model': 'Teana',
#     'engin': 'gasolin'
# }

# print('brand' in my_dict)

# print('year' in my_dict)

# print('year' not in my_dict)


# my_num = 10
# a = -15

# print(+my_num)

# my_bool = False
# print(+ my_bool)

# print(not my_num)
# print(- my_num)
# print(a and my_num)


# a = [1, 2]
# b = [1, 2]

# print(a == b)
# print(a.__eq__(b))
# print(a is b)


# a = 10
# b = a

# c = a+b
# print(a is b, id(a) == id(b))
# print(c is a)


# Области видимости
# c = 13


# def my_fn(a, b):
#     print(c)
#     print(a)

#     print(b)
#     print(dir())


# my_fn('abc', 'xyz')

# from copy import deepcopy

# info = {'name': 'Zviadi',
#         'is_student': True,
#         'reviews': []
#         }
# info_deepcopy = deepcopy(info)
# info_deepcopy['sername'] = 'Shchukin'
# info_deepcopy['reviews'].append('Great job')

# info['new_key'] = 10
# info['name'] = 'katy'


# print(info)
# print(id(info))

# print(info_deepcopy)
# print(id(info_deepcopy))
