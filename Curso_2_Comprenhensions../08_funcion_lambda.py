def increment(x):
    return x + 1

func_1 = increment(10)
print(func_1)

func_2 = lambda x:x+1
print(func_2(5))

full_name = lambda name, last_name: f' El nombre completo es {last_name.title()} {name.title()}'
print(full_name('Elva','Nanon'))
