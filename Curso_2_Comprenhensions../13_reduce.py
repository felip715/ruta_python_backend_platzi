import functools

numbers = [1, 2, 3, 4]

sum_of_numbers = functools.reduce(lambda counter, item: counter + item, numbers)

print(sum_of_numbers)

# counter es el resultado que se va sumando entre el item actual y la suma que se esta acarreando

def acum(counter, item):
    print(f'counter -> {counter}')
    print(f'item -> {item}')
    return counter + item

sum_of_numbers = functools.reduce(acum, numbers)

print(sum_of_numbers)