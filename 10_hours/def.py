def send_data(date):
    # sending data to the remote server
    pass


# def process_data(input_data, send_data_fn):
#     updated_data = input_data.copy()
#     # action with updated_data
#     send_data_fn(updated_data)


# process_data({'name': 'Zviadi'}, send_data)


# def print_number_info(num):
#     """
#     Prints num information


#     Args:
#         num (int): integer number

#     Returns:
#         int: Same number
#     """
#     if (num % 2) == 0:
#         print('Entered number is even')
#     else:
#         print('Entered number is odd')
#     return num


# print_number_info(20)


# def print_square_num(num):
#     print("Square of the num is", num*num)


# def process_number(num, calback_fn):
#     calback_fn(num)


# entered_num = int(input('Enter any number: '))

# process_number(entered_num, print_number_info)


# process_number(entered_num, print_square_num)


# from datetime import date


# def get_weekday():
#     return date.today().strftime('%A')


# def create_new_post(post, weekday=get_weekday()):
#     post_copy = post.copy()
#     post_copy['create_on_weekday'] = weekday
#     return post_copy


# initial_post = {'id': 123, 'author': 'Zviadi'}

# post_with_weeday = create_new_post(initial_post)
# print(post_with_weeday)


# from datetime import date

# print(date.today())


# def update_car_info(**car):
#     car['is_availabel'] = True
#     return car


# print(update_car_info(brand="nissan", price=16_000))


# def merge_list_to_dict(list_1, list_2):
#     list1_copy = list_1.copy()
#     list2_copy = list_2.copy()
#     dict_zip = dict(zip(list1_copy, list2_copy))
#     return dict_zip

# test_list = [1, 2, 3, 4, 5]
# result_list = [True, False, False, True]

# print(merge_list_to_dict(list_1=test_list, list_2=result_list))

# print(merge_list_to_dict(test_list, list_2=result_list))


# def get_posts_info(**person):
#     print(person)
#     print(type(person))
#     info = (
#         f"{person['name']} wrote"
#         f"{person['posts_qty']} posts"
#     )
#     return info


# info = get_posts_info(name='Zviadi', posts_qty=25)
# print(info)


# def get_posts_info(**person):
#     print(person)
#     info = f"{person['name']} wrote {person['posts_qty']} posts"
#     return info


# info = get_posts_info(name='Zviadi', posts_qty=4, id=123.233)
# print(info)


# def sum_nums(*args):
#     print(args)
#     print(type(args))

#     print(args[0])
#     return sum(args)


# print(sum_nums())


# def in_pers_age(person):
#     person_copy = person.copy()
#     person_copy['age'] += 1
#     print(id(person_copy))
#     return person_copy

# person_one = {'name': 'Bob', 'age': 21}
# print(person_one['age'])

# new_person = in_pers_age(person_one)
# print(new_person)
# print(id(new_person))
# print(person_one )
# print(id(person_one))


# def my_fn(a, b):
#     print(id(a))
#     a += 1
#     print(id(a))
#     c = a + b
#     print(b)
#     print(a)
#     print(id(b))
#     return c

# num_one = 10
# num_two = 5

# res = my_fn(num_one, num_two)

# print(res)
# print(num_one)
# print(id(num_two))
