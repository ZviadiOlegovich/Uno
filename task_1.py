# set_1 = {32, 45, 56, 87}
# set_2 = set_1.copy()
# # set_2.add(34)
# print(set_1 == set_2)  # Последовательности имет одинаковые данные
# print(set_1 is set_2)  # Пос-ти это разные обьекты с разными ID
# print(id(set_2), id(set_1))
# print(446 in set_2)


# task 2
my_dict = {'brand': 'Nissan',
           'model': 'Teana',
           'engin': 'gasolin'}

your_dict = {'model': 'Teana',
             'brand': 'Nissan',
             'engin': 'gasolin'}

your_dict == my_dict and print('Dict are equal')
