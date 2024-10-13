# START
import random

# a
rand_list: list[bool] = [random.choice([True, False]) for _ in range(3)]
print(rand_list)

# b -check if the entire list is True
print(all(rand_list))

# c - check if there is at least 1 True
print(any(rand_list))

# d - check if the entire list is False
print(not any(rand_list))

# e - check if there is at least 1 False
print(not all(rand_list))

# f
rand_num: list[int] = [random.randint(-2, 2) for _ in range(5)]
print(rand_num)

# g - check if list contains only ! = 0
print(all(rand_num))

# h - check if at least one num is ! = 0
print(any(rand_num))

# i - check if the list contains only 0
print(not any(rand_num))

# j - check if at least one num is 0
print(not all(rand_num))

# STOP
