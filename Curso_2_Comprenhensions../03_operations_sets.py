# Create
set_a = {'Argentina', 'Paraguay', 'Brasil'}
print(f'Original_1: {set_a}')

set_b = {'Argentina', 'Paraguay', 'Peru'}
print(f'Original_2: {set_b}')

#Union, tambien se puede realizar con  |
print(f'La union es: ',set_a.union(set_b))
print(f'La union es: ',set_a | set_b)

#Interseccion, los elementos en comun
print(f'La interseccion es: ',set_a.intersection(set_b))
print(f'La interseccion es: ',set_a & set_b)

#Diferencia, los elementos disntintos que a tiene de b
print(f'La diferencia es: ',set_a.difference(set_b))
print(f'La diferencia es: ',set_a - set_b)

#Diferencia simetrica, los elementos que no tienen en comun ambos conjuntos
print(f'La diferencia simetrica es: ',set_a.symmetric_difference(set_b))
print(f'La diferencia simetrica es: ',set_a ^ set_b)
