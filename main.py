# is_magician = True
# is_expert = True

# if is_magician and is_expert:
#     print("You are a master magician")
# elif is_magician and not is_expert:
#     print('At least you are a getting there')
# elif not is_magician and not is_magician:
#     print('You need magic powers')


# Exercise: Check for duplicates inlist:
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'm', 'a']

# for i in range(0, len(some_list)):
#     for j in range(i + 1, len(some_list)):
#         if some_list[i] == some_list[j]:
#             print(some_list[i])
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
