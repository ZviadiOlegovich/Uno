# def scramble(s1, s2):
#     sList = list(s1)
#     nList = list(s2)
#     for n in nList:
#         if n in sList:
#             sList.remove(n)
#         else:
#             return False
#     return True
s1 = "abcdefghijklmnopqrstuvwxyz" * 10000
s2 = "zyxcba" * 9000


# print(scramble(s1, s2))
# def next_pal(val):
#     for i in range(100000):
#         n_p = str(i)
#         rev_n_p = ''.join(reversed(n_p))
#         if n_p == rev_n_p:
#             return n_p


# print(next_pal(22))
# a = [-3, 0, 2, 4, 5, 4, 23, 65, 1, 432, 65, 42, 21, 2,
#      2, 32, 43, 65, 87, 43, 21, 54, 65, 54, 2, 132, 7]
# a.sort()
# print(a)
# value = 12


# def binary_search(list, item):
#     low = 0
#     high = len(list) - 1
#     i = 0
#     while low <= high:
#         mid = (low + high) // 2
#         guess = list[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#         i = i+1
#     return False


# def sum_num(l, n):
#     list_num = l
#     list_num.sort()
#     find_num = []
#     for i in list_num:
#         num1 = n - i
#         index_1 = binary_search(list_num, num1)
#         if list_num[index_1] == num1:
#             find_num = [i, num1]
#             return print(f"numbers found {find_num}")
#     return print('numbers not found')
# list_1 = [-1, -3, 0, 2, 6, 9]
# num = 6

# # sum_num(list_1, num)


# def two_sum(lis, k):
#     l = 0
#     r = len(lis) - 1
#     while l < r:
#         sum_num = lis[l]+lis[r]
#         if sum_num == k:
#             return [lis[l], lis[r]]
#         if sum_num < k:
#             l += 1
#         else:
#             r -= 1
#     return []


# print(two_sum(list_1, num))
# from collections import Counter


# def find_lowest_int(k):
#     n = 9
#     while Counter(str(k * n)) != Counter(str(k * n + n)):
#         n += 9
#     return n


# k1 = 325
# print(find_lowest_int(k1))

# list1 = [1, 2, 'aasf', '1', '123', 123]

# def filter_list(l):
#     l = [num for num in l if type(num) is int]
#     return l

# print(filter_list(list1))

# print(filter_list(list1))

# def get_sum(a, b):
#     return sum(range(min(a, b), max(a, b) + 1))

# print(get_sum(0, 3))

# test1 = 'This kata is very interesting!'
# n = 1

# def encrypt(text, n):
#     encrypted = text
#     for i in range(n):
#         text1 = list(encrypted)
#         encrypted = text1[1::2] + text1[::2]
#         encrypted = ''.join(encrypted)

#     return encrypted

# def decrypt(text, n):
#     if n <= 0:
#         return text
#     return encrypt(text, 4 - (n+4) % 4)

# def decrypt2(text, n):
#     if n <= 0:
#         return text
#     return encrypt(text, 8 - (n+8) % 8)

# encrypted = encrypt(test1, n)

# print(encrypted)
# print('\n')
# print(decrypt2(encrypted, n))

# encrypted_text = encrypt(test1, n)
# print(encrypt(test1, n))

# def digital_root(n):
#     return n % 9 or n and 9

# print(digital_root(100))

# def digital_root(n):
#     if len(str(n)) > 1:
#         num_sum = 0
#         for i in list(str(n)):
#             num_sum += int(i)
#         return digital_root(num_sum)
#     else:
#         return n
# s1 = list("katas")
# s2 = list("steak")

# print(subfinder(s1, s2))
# s1 = "abcdefghijklmnopqrstuvwxyz" * 10000
# s2 = "zyxcba" * 9000

# list_2 = list(s2)
# list_1 = list(s1)


# scramble(s1, s2)
# print(scramble(s1, s2))
# def sublist_in_list(sub, lis):
#     sub = list(sub)
#     lis = list(lis)
#     sub.sort()
#     lis.sort()
#     return str(sub).strip('[]') in str(lis).strip('[]')

# print(sublist_in_list(s2, s1))

# print(dict_zip_1)
# if (dict_zip_2.keys() - dict_zip_1.keys())

# print(list_2)
# dict_1 = {'q': 2, 'a': 3}
# dict_2 = {'q': 2, 'a': 3, }
# print(dict_1 == dict_2)

# def scramble(s1, s2):
#     list_2 = list(s2)
#     list_1 = list(s1)
#     list_3 = []
#     for i in list_2:
#         if i in list_1:
#             list_3.append(i)
#             list_1.remove(i)
#     if list_2.sort() is list_3.sort():
#         print(list_2)
#         print(list_3)
#         return True

#     else:
#         print(list_3)
#         return False

# s1 = "jscripts"
# s2 = "javascript"

# print(scramble(s1, s2))

# def solution(start, finish):
#     dif_shel = finish - start
#     dif_shel = int(dif_shel/3 + dif_shel % 3)
#     return dif_shel

# print(solution(429, 449))

# def digital_root(n):
#     if len(str(n)) > 1:
#         num_sum = 0
#         for i in list(str(n)):
#             num_sum += int(i)
#         return digital_root(num_sum)
#     else:
#         return n

# def even_or_odd(number):
#     if number % 2:
#         return 'Odd'
#     else:
#         return 'Even'

# print(even_or_odd(234))
