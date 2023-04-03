numbers = [1, 2, 3, 4]

numbers_v2 = list(map(lambda x: x * 2, numbers ))

print(numbers_v2)

numbers_2 = [5, 6, 7]

numbers_v3 = list(map(lambda x, y: x + y, numbers, numbers_2))
print(numbers_v3)