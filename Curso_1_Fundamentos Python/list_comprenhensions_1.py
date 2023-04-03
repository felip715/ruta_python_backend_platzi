my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

# Escribe tu solución 👇
#for i in my_list:
pos_num = [i for i in my_list if i%2 == 0]
new_list.append(pos_num)

print(new_list)