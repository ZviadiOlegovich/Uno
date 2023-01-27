# def digital_root(n):
# print (len(345))
# n = 345
# str_n = str(n)
# list_n = list(str_n)
# sum_num = 0
# if len(list(str(sum_num))) > 1:
#     list_sum_num = list(str(sum_num))
#     digital_root(list_sum_num)
# else:
#     print(sum_num)

# def listsum(n):
#     num_sum = 0
#     for i in list(str(n)):
#         num_sum += int(i)
#     return num_sum


# def rec_droot(n):
#     if len(str(n)) > 1:
#         n = listsum(n)
#         return rec_droot(n)
#     else:
#         return n


# def rec_droot(n):
#     if len(str(n)) > 1:
#         num_sum = 0
#         for i in list(str(n)):
#             num_sum += int(i)
#         return rec_droot(num_sum)
#     else:
#         return n


# # print(digital_root(109))
# a = 123
# print(rec_droot(a))

# def digital_root(n):
#     sum_num = 0
#     num_inp = list(str(n))
#     if len(num_inp) != 1:
#         for i in num_inp:
#             sum_num += int(i)

#     else:
#         print(sum_num)
#         return sum_num


# print(digital_root(num1))


# n = 12345
# p = str(n)
# list_n = list(p)


# def even_or_odd(number):
#     if number % 2:
#         return 'Odd'
#     else:
#         return 'Even'


# print(even_or_odd(4))
# def litres(time):
#     round_lit = int(time/2)
#     return round_lit


# time = 3.4
# ans = litres(time)
# print(ans)

# bundle = ["vanilla latte", "vanilla scone"]

# matcha_1 = []
# for item in bundle:
#     update = item.replace("vanilla", "matcha")
#     matcha_1.append(update)

# print(matcha_1)
# matcha_2 = [item.replace("vanilla", "matcha") for item in bundle]
# print(matcha_2)

# answers = [True, False, False]
# opposite = {not answer for answer in answers}
# print(opposite)

# words = ['all knowing', 'ex president', 'self expression']


# def add_hyphen(word):
#     parts = word.split(' ')
#     return parts[0]+'-'+parts[1]


# hyphen_words = [add_hyphen(word) for word in words]
# print(hyphen_words)
