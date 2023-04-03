import random
names = ['Chizo', 'Tete', 'Tanque']
ages = [random.randint(40, 60) for name in names]

# Podemos generar una lista de tuplas con la union entre las dos listas
info = zip(names,ages)
print(list(info))

dict_ = {name: age for (name, age) in zip(names,ages)}

print(dict_)

# Tambien podemos tener una condicion a cumplir

new_info = {names: ages for (names, ages) in dict_.items() if ages > 50}

print(new_info)