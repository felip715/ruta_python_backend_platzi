# Create
set_countries = {'Argentina', 'Paraguay', 'Brasil', 'EEUU'}
print(f'Original: {set_countries}')

# Remove, da error al no encontrar el elemento
set_countries.remove('EEUU')
print(f'Removido EEUU: {set_countries}')
# Discard, no da error si no encuentra el elemento
set_countries.discard('Canada')
print(f'Trata de remover Canada: {set_countries}')

# Add
set_countries.add('Uruguay')
print(f'Agregado Uruguay: {set_countries}')

# Update
set_countries.update({'Uruguay', 'Peru', 'Chile'})
print(f'Set actualizado: {set_countries}')

